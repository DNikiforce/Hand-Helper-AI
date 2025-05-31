from telegram import Update
from telegram.ext import ContextTypes
from context.session import GameSessionManager
from utils.parser import parse_hand

session_manager = GameSessionManager()

async def handle_preflop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = session_manager.get(update.effective_user.id)
    text = update.message.text
    hand = parse_hand(text)
    session.set_hand(hand)
    await update.message.reply_text("🃏 Рука получена. Теперь введи FLO:")