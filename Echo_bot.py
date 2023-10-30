# pip install pyTelegramBotAPI

import telebot

bot = telebot.TeleBot("Вставить свой токен")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Привет, я Эхо.\nЯ буду повторять за тобой сообщения.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
