# PokerBot 🤖♠️

Telegram-бот для анализа кэш-рук на лимите $1/$3.  
Использует Telegram API, FastAPI, распознавание речи и OpenAI.

## Установка

1. Установи Python 3.10+
2. Установи зависимости:
```
pip install -r requirements.txt
```
3. Создай файл `.env` на основе `.env.example`
4. Запусти локально:
```
uvicorn main:app --reload
```

## Команды
- PF: A♠ K♠
- FLO: 7♦ T♣ 3♠
- POS: CO vs BB
- OPP: TAG

Голосовые сообщения тоже поддерживаются!
