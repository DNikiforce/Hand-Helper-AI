from telegram import Update
from telegram.ext import ContextTypes
from context.session import GameSessionManager

session_manager = GameSessionManager()

async def handle_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = session_manager.get(update.effective_user.id)
    session.reset()

    await update.message.reply_text("✅ Результат зафиксирован. Сессия обнулена. Можешь ввести новую раздачу (PF:).")
