from telegram import Update
from telegram.ext import ContextTypes

HELP_TEXT = '''
🧠 <b>Команды ввода рук:</b>
PF: Preflop (пример: PF: A♠ K♠)
FLO: Flop (пример: FLO: 7♦ T♣ 3♠)
TUR: Turn (пример: TUR: 2♣)
RIV: River (пример: RIV: 8♥)
POS: Позиции (пример: POS: CO vs BB)
OPP: Тип оппонента (пример: OPP: TAG)
RES: Результат (пример: RES: lost)
'''

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode="HTML")
