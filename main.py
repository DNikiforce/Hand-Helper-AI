import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, ContextTypes
)

from context.session import GameSessionManager
from handlers.preflop import handle_preflop
from handlers.flop import handle_flop
from handlers.turn import handle_turn
from handlers.river import handle_river
from handlers.result import handle_result
from handlers.help import help_command
from handlers.speech.recognize import handle_voice

# Создаём глобальный менеджер сессий пользователей
session_manager = GameSessionManager()

# ✨ Функция /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Отправь текст или голос, я дам разбор руки.")

# Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") + WEBHOOK_PATH

# Инициализация Telegram бота
application = Application.builder().token(TOKEN).build()

# Инициализация FastAPI
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.Regex(r"^PF:"), handle_preflop))
    application.add_handler(MessageHandler(filters.Regex(r"^FLO:"), handle_flop))
    application.add_handler(MessageHandler(filters.Regex(r"^TUR:"), handle_turn))
    application.add_handler(MessageHandler(filters.Regex(r"^RIV:"), handle_river))
    application.add_handler(MessageHandler(filters.Regex(r"^RES:"), handle_result))

    await application.initialize()
    await application.start()
    await application.bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await application.stop()

@app.post(WEBHOOK_PATH)
async def handle_webhook(request: Request):
    update = Update.de_json(await request.json(), application.bot)
    await application.process_update(update)
    return "ok"
