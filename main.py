import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalam-o-Alaikum! Aap ka free bot mobile se bilkul sahi chal gaya hai!")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"Aap ne kaha: {message.text}")

bot.infinity_polling()
