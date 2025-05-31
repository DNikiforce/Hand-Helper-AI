from telegram import Update
from telegram.ext import ContextTypes
from logic.recommendation import recommend_bet
from context.session import GameSessionManager
from utils.parser import parse_board
from logic.equity import calculate_equity_and_outs

session_manager = GameSessionManager()

async def handle_river(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = session_manager.get(update.effective_user.id)
    board = parse_board(update.message.text)
    session.add_board_cards(board)

    if not session.hand:
        await update.message.reply_text("❗️Сначала введи свою руку (PF).")
        return

    equity, outs = calculate_equity_and_outs(
        session.hand, session.board, session.multi_count
    )

    bet = recommend_bet(equity, 'river', session.is_multi, session.position)

    await update.message.reply_text(
        f"🧮 Equity: {equity}%\n🎯 Outs: {outs}\n💬 Bet: {bet}"
    )

