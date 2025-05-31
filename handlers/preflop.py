from telegram import Update
from telegram.ext import ContextTypes
from context.session import GameSessionManager
from utils.parser import parse_hand

session_manager = GameSessionManager()

async def handle_preflop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = session_manager.get(update.effective_user.id)
    text = update.message.text.strip()

    if text.startswith("POS:"):
        session.set_position(text[4:].strip())
        await update.message.reply_text("📌 Позиция установлена.")
        return

    if text.startswith("OPP:"):
        session.set_opponent(text[4:].strip())
        await update.message.reply_text("👤 Тип оппонента установлен.")
        return

    hand = parse_hand(text)
    session.set_hand(hand)

    await update.message.reply_text("🤝 Рука получена. Теперь введи FLO:")

