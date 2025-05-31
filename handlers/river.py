from telegram import Update
from telegram.ext import ContextTypes
from logic.recommendation import recommend_bet
from context.session import session_manager
from utils.parser import parse_board
from logic.equity import calculate_equity_and_outs
from logic.strategy_tip import get_strategy_tip

async def handle_river(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = session_manager.get(user_id)

    # Проверка на наличие стартовой руки
    if not session.hand:
        await update.message.reply_text("⚠️ Сначала введи свою руку (PF).")
        return

    # Парсим и добавляем карты борда
    board = parse_board(update.message.text)
    if not board:
        await update.message.reply_text("❌ Неверный формат борда. Пример: RIV: 2h 7d Jc 9s Ah")
        return

    session.add_board_cards(board)

    # Считаем equity, outs и даём рекомендацию
    equity, outs = calculate_equity_and_outs(
        session.hand, session.board, session.multi_count
    )
    bet = recommend_bet(equity, 'river', session.is_multi, session.position)
    tip = get_strategy_tip(session.opponent_type, 'river')

    await update.message.reply_text(
        f"📊 Equity: {equity}%\n"
        f"🎯 Outs: {outs}\n"
        f"💰 Bet: {bet}\n"
        f"🧠 {tip}"
    )
