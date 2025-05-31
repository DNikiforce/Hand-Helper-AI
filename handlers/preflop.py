from telegram import Update
from telegram.ext import ContextTypes
from utils.parser import parse_hand
from context.session import session_manager

async def handle_preflop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = session_manager.get(user_id)
    text = update.message.text.strip()

    # Установка позиции
    if text.startswith("POS:"):
        session.set_position(text[4:].strip())
        await update.message.reply_text("📌 Позиция установлена.")
        return

    # Установка типа оппонента
    if text.startswith("OPP:"):
        session.set_opponent(text[4:].strip())
        await update.message.reply_text("👤 Тип оппонента установлен.")
        return

    # Установка руки (обязательный префикс PF:)
    if text.startswith("PF:"):
        hand = parse_hand(text)
        if hand:
            session.set_hand(hand)
            await update.message.reply_text("🤝 Рука получена. Теперь введи FLO:")
        else:
            await update.message.reply_text("❌ Неверный формат руки. Пример: PF:Ah Kh")
        return

    # Ответ по умолчанию — если текст не подошёл ни под один формат
    await update.message.reply_text("⚠️ Не понял. Введи: PF:Ah Kh, POS: IP, OPP: LAG и т.д.")

