import os
import telebot
import random
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

# Get bot token from .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Sample horoscope messages
horoscopes = {
    "aries": ["🔥 Aries, today is your day to shine!", "💪 Stay strong and confident, Aries!"],
    "taurus": ["🌿 Taurus, patience will lead to success!", "💰 A financial surprise is coming your way, Taurus!"],
    "gemini": ["🗣 Gemini, today is perfect for communication!", "📖 A new learning opportunity awaits you, Gemini!"],
    "cancer": ["💙 Cancer, focus on self-care today!", "🏠 Home brings peace and happiness today, Cancer!"],
    "leo": ["🌞 Leo, your energy is magnetic today!", "🎭 A creative spark will inspire you, Leo!"],
    "virgo": ["📋 Virgo, organization is your superpower today!", "⚡ Take a risk and step out of your comfort zone, Virgo!"],
    "libra": ["⚖️ Libra, balance is key to your success today!", "❤️ Love and romance are in the air, Libra!"],
    "scorpio": ["🔥 Scorpio, passion will drive your actions today!", "🔍 A hidden truth will be revealed, Scorpio!"],
    "sagittarius": ["🏹 Sagittarius, adventure awaits!", "✈️ A travel opportunity is coming, Sagittarius!"],
    "capricorn": ["🏆 Capricorn, stay focused on your goals!", "📈 Hard work will bring rewards, Capricorn!"],
    "aquarius": ["🌊 Aquarius, embrace your uniqueness today!", "🔬 An innovative idea will strike, Aquarius!"],
    "pisces": ["🌊 Pisces, your intuition is strong today!", "🎨 A creative project will bring joy, Pisces!"]
}

# Zodiac compatibility pairs (just for fun!)
compatibility = {
    ("aries", "leo"): "🔥 A fiery and passionate match! Lots of excitement ahead!",
    ("taurus", "virgo"): "🌿 A stable and practical duo! You complete each other well.",
    ("gemini", "libra"): "💬 Great communication and balance in this relationship!",
    ("cancer", "pisces"): "💙 A deep emotional connection! A true soulmate bond.",
    ("leo", "sagittarius"): "🌟 A dynamic power couple! Endless adventures await!",
    ("virgo", "capricorn"): "💼 Hardworking and ambitious! You build a future together.",
    ("libra", "aquarius"): "🌈 A creative and intellectual match! So much fun ahead.",
    ("scorpio", "cancer"): "🔥 Passion and depth! A powerful emotional connection.",
    ("sagittarius", "aries"): "🏹 A fun and spontaneous match! Always on the go!",
    ("capricorn", "taurus"): "💪 A strong and reliable duo! You understand each other deeply.",
    ("aquarius", "gemini"): "💡 An innovative and lively pair! Lots of intellectual chemistry.",
    ("pisces", "scorpio"): "🌊 A deep, spiritual connection! Intense and magical love.",
}

# Random quotes for motivation
quotes = [
    "✨ Believe in yourself and all that you are!",
    "🌟 The best way to predict the future is to create it.",
    "🔥 You are capable of amazing things!",
    "💪 Hardships often prepare ordinary people for an extraordinary destiny.",
    "🌈 Keep going. Everything you need will come to you at the perfect time."
]

# Fun random replies
fun_responses = [
    "🤷‍♂️ I don't know what to say either, lil bro.",
    "👁️ EYE OF RAHHH",
    "💯 Facts, very sigma of you.",
    "🛎️ LINGGANG GULI GULI WACHA LINGGANG GU"
]

# Lucky numbers generator
def get_lucky_numbers():
    return f"🎲 Your lucky numbers for today are: {random.sample(range(1, 50), 5)}"

# Start/Hello command
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey there!🌟 I'm your daily horoscope bot. 🔮\n\n"
                          "Use `/horoscope <your zodiac sign>` to get today's prediction.\n"
                          "Example: `/horoscope aries`\n\n"
                          "Want to check zodiac compatibility? Try `/compatibility leo aries`\n"
                          "Need some luck? Get `/lucky_numbers`!\n"
                          "Feeling down? Type `/quote` for motivation!")

# Horoscope command
@bot.message_handler(commands=['horoscope'])
def send_horoscope(message):
    try:
        sign = message.text.split()[1].lower()
        if sign in horoscopes:
            bot.reply_to(message, random.choice(horoscopes[sign]))
        else:
            bot.reply_to(message, "⚠️ Please enter a valid zodiac sign! (e.g., `/horoscope leo`)")
    except IndexError:
        bot.reply_to(message, "⚠️ Please provide your zodiac sign. Example: `/horoscope pisces`")

# Sample jokes
joke = [
    "Why don't skeletons fight each other? Because they don't have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

# Fun facts
facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still good!",
    "Octopuses have three hearts!",
    "Bananas are berries, but strawberries aren't!"
]

# Magic 8-ball responses
eight_ball_responses = [
    "Yes, definitely!",
    "No way!",
    "Ask again later...",
    "It is certain!",
    "Very doubtful...",
    "Without a doubt!",
    "Better not tell you now."
]

# Compatibility command
@bot.message_handler(commands=['compatibility'])
def check_compatibility(message):
    try:
        sign1, sign2 = message.text.split()[1].lower(), message.text.split()[2].lower()
        if (sign1, sign2) in compatibility or (sign2, sign1) in compatibility:
            match = compatibility.get((sign1, sign2)) or compatibility.get((sign2, sign1))
            bot.reply_to(message, f"💞 Compatibility between {sign1.capitalize()} and {sign2.capitalize()}:\n{match}")
        else:
            bot.reply_to(message, "🤔 I couldn't find a compatibility match. Try different signs!")
    except IndexError:
        bot.reply_to(message, "⚠️ Please provide two zodiac signs. Example: `/compatibility leo aries`")

# Lucky numbers command
@bot.message_handler(commands=['lucky_numbers'])
def lucky_numbers(message):
    bot.reply_to(message, get_lucky_numbers())

# Quote command
@bot.message_handler(commands=['quote'])
def send_quote(message):
    bot.reply_to(message, random.choice(quotes))

# About command
@bot.message_handler(commands=['about'])
def about_bot(message):
    bot.reply_to(message, "🔮 I'm a bot that provides daily horoscopes, zodiac compatibility, "
                          "lucky numbers, and motivation! Type `/horoscope <zodiac>` to get started.")

# Joke command
@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, random.choice(joke))

# Fun fact command
@bot.message_handler(commands=['fact'])
def send_fact(message):
    bot.reply_to(message, random.choice(facts))

# Decision Maker command
@bot.message_handler(commands=['decide'])
def decide(message):
    try:
        options = message.text.split()[1:]
        if len(options) < 2:
            bot.reply_to(message, "⚠️ Please provide two options. Example: `/decide pizza burger`")
        else:
            bot.reply_to(message, f"🎲 I choose: {random.choice(options)}!")
    except IndexError:
        bot.reply_to(message, "⚠️ Please provide two options. Example: `/decide tea coffee`")

# Dice Roller command
@bot.message_handler(commands=['roll_dice'])
def roll_dice(message):
    bot.reply_to(message, f"🎲 You rolled a {random.randint(1, 6)}!")

# Magic 8-Ball command
@bot.message_handler(commands=['8ball'])
def eight_ball(message):
    try:
        question = " ".join(message.text.split()[1:])
        if question:
            bot.reply_to(message, f"🔮 {random.choice(eight_ball_responses)}")
        else:
            bot.reply_to(message, "⚠️ Please ask a yes/no question. Example: `/8ball Will I be rich?`")
    except IndexError:
        bot.reply_to(message, "⚠️ Please ask a yes/no question. Example: `/8ball Will I get an A?`")

# Weather command
@bot.message_handler(commands=['weather'])
def get_weather(message):
    try:
        location = message.text.split(maxsplit=1)[1]  # Extract location from command
        url = f"https://wttr.in/{location}?format=%C+%t"
        response = requests.get(url)

        if response.status_code == 200:
            bot.reply_to(message, f"🌤 Weather in {location}: {response.text}")
        else:
            bot.reply_to(message, "⚠️ Could not fetch weather. Try another location.")
    except IndexError:
        bot.reply_to(message, "⚠️ Please provide a location. Example: `/weather Kuala Lumpur`")

# Handle unknown commands
@bot.message_handler(func=lambda message: message.text.startswith("/"))
def unknown_command(message):
    bot.reply_to(message, "⚠️ Unknown command. Type `/horoscope <zodiac>` for your daily horoscope!")

# Echo all other text messages with fun responses
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, random.choice(fun_responses))

# Keep bot running
print("The bot is running...")
bot.infinity_polling()
