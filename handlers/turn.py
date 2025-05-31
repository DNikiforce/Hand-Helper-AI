from telegram import Update
from telegram.ext import ContextTypes
from context.session import GameSessionManager
from logic.equity import calculate_equity_and_outs

session_manager = GameSessionManager()

async def handle_turn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text

    session_manager.update_stage(user_id, 'turn', message)
    session = session_manager.get_session(user_id)

    result = calculate_equity_and_outs(session)
    await update.message.reply_text(result)
