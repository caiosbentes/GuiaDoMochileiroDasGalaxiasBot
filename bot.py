import telebot

TOKEN = '<api_token>'

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Envie algo e receba o significado da vida, do universo e tudo mais...")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, '42')

bot.polling()
