import os
from fastapi import FastAPI
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from handlers.help import help_command
from handlers.preflop import handle_preflop
from speech.recognize import handle_voice

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
app = FastAPI()
telegram_app = Application.builder().token(TOKEN).build()

@app.on_event("startup")
async def on_startup():
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CommandHandler("help", help_command))
    telegram_app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_preflop))
    await telegram_app.initialize()
    await telegram_app.start()

@app.on_event("shutdown")
async def on_shutdown():
    await telegram_app.stop()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Отправь текст или голос, я дам разбор руки.")
