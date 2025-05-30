from telegram import Update
from telegram.ext import ContextTypes

async def handle_preflop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"📥 Получена текстовая раздача:\n{text}")


