from telegram import Update
from telegram.ext import ContextTypes
from context.session import session_manager

async def handle_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().upper()
    
    # Проверка на корректность результата
    if not (text.startswith("RES: WIN") or text.startswith("RES: LOSE")):
        await update.message.reply_text("⚠️ Используй: RES: WIN или RES: LOSE")
        return

    session = session_manager.get(update.effective_user.id)
    session.reset()

    await update.message.reply_text(
        "✅ Результат зафиксирован. Сессия обнулена. Можешь ввести новую раздачу (PF:)."
    )

