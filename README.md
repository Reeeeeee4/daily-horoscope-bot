# 🌟 Telegram Horoscope Bot 🤖

An easy Telegram bot that provides daily horoscope readings for different zodiac signs. Built using Python and the Telegram Bot API.

## 📌 Table of Contents
- [🚀 Features](#-features)
- [🛠 Setup & Installation](#-setup--installation)
- [📜 Example Commands](#-example-commands)
- [📖 Resources](#-resources)
- [🎯 Future Improvements](#-future-improvements)
- [📜 Note](#-note)

## 🚀 Features
- Get daily horoscope readings for all 12 zodiac signs.
- **New:** Check zodiac compatibility with `/compatibility <sign1> <sign2>`.
- **New:** Generate lucky numbers with `/lucky_numbers`.
- **New:** Get a random motivational quote with `/quote`.
- **New:** Ask the Magic 8-Ball for a yes/no answer with `/8ball <question>`.
- **New:** Get a random joke with `/joke` and fun facts with `/fact`.
- **New:** Weather updates using `/weather <location>`.
- **New:** Decision Maker - Let the bot choose for you! `/decide option1 option2`
- **New:** Dice Roller - Roll a virtual dice with `/roll_dice`.
- Simple and interactive Telegram bot interface.
- Built using Python and `python-telegram-bot` library.

## 🛠 Setup & Installation

### Prerequisites
- Python 3.x installed
- A Telegram bot token (Create one via [BotFather](https://t.me/BotFather))

### Installation Steps
Clone this repository:
```bash
git clone https://github.com/yourusername/telegram-horoscope-bot.git
cd telegram-horoscope-bot
```

Install dependencies:
```bash
pip install python-telegram-bot requests python-dotenv
```

Create a `.env` file and add your Telegram bot token:
```ini
BOT_TOKEN=your_telegram_bot_token
```

Run the bot:
```bash
python bot.py
```

## 📜 Example Commands
```bash
/start - Start the bot
/horoscope <zodiac_sign> - Get daily horoscope (e.g., /horoscope aries)
/compatibility <sign1> <sign2> - Check zodiac compatibility
/lucky_numbers - Get your lucky numbers
/quote - Receive a motivational quote
/8ball <question> - Magic 8-Ball answers your yes/no question
/joke - Get a random joke
/fact - Learn a fun fact
/weather <location> - Get real-time weather updates
/decide <option1> <option2> - Let the bot make a decision
/roll_dice - Roll a virtual dice
/about - Learn more about the bot
```

## 📖 Resources
- [FreeCodeCamp Telegram Bot Tutorial](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 🎯 Future Improvements
- Add horoscope source customization.
- Provide weekly and monthly horoscopes.
- Integrate AI-generated horoscope predictions.
- Improve joke and fact database.

## 📜 Note
This is a personal project and not intended for commercial use.

💫 **Created with 💖**
