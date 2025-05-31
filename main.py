import os
from context.session import GameSessionManager
# Создаём глобальный менеджер сессий пользователей
session_manager = GameSessionManager()
from logic.equity import calculate_equity_and_outs
from utils.parser import parse_cards_from_emojis
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, ContextTypes
)
from dotenv import load_dotenv
from handlers.help import help_command
from handlers.preflop import handle_preflop
from handlers.speech.recognize import handle_voice

# Загрузка переменных окружения
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") + WEBHOOK_PATH

# Инициализация Telegram бота
application = Application.builder().token(TOKEN).build()

# Регистрируем FastAPI
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_preflop))
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await application.stop()

# Webhook входящий запрос
@app.post(WEBHOOK_PATH)
async def handle_webhook(request: Request):
    update = Update.de_json(await request.json(), application.bot)
    await application.process_update(update)
    return "ok"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Отправь текст или голос, я дам разбор руки.")
