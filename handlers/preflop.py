from telegram import Update
from telegram.ext import ContextTypes
from context.session import GameSessionManager

session_manager = GameSessionManager()

async def handle_preflop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text

    # Пример ввода: PF: A♠ K♣ POS: CO vs BB OPP: TAG
    session_manager.start_new_session(user_id)
    session_manager.update_stage(user_id, 'preflop', message)

    await update.message.reply_text("✍️ Префлоп сохранён.")

