import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from dotenv import load_dotenv

from handlers.help import help_command
from handlers.preflop import handle_preflop
from speech.recognize import handle_voice

# Загружаем переменные окружения (.env)
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") + WEBHOOK_PATH  # добавь в Railway переменную WEBHOOK_URL

# Telegram App
application = Application.builder().token(TOKEN).build()

# FastAPI App
app = FastAPI()

@app.post(WEBHOOK_PATH)
async def receive_update(request: Request):
    json_data = await request.json()
    update = Update.de_json(json_data, application.bot)
    await application.process_update(update)
    return {"ok": True}

# Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.VOICE, handle_voice))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_preflop))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Отправь текст или голос, и дам разбор руки.")

@app.on_event("startup")
async def on_startup():
    await application.initialize()
    await application.bot.set_webhook(url=WEBHOOK_URL)
    await application.start()
    print("✅ Бот запущен (Webhook)")

@app.on_event("shutdown")
async def on_shutdown():
    await application.stop()
    print("❌ Бот остановлен")

