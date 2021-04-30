import telebot

bot = telebot.TeleBot("982445371:AAGLsP22TafPHCVOZj2mBzSIfoxul1i5rVI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
