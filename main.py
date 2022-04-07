# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
from telebot import apihelper

# apihelper.proxy = {
#     'https': 'socks5h://127.127.127.127:12345'
# }



TOKEN = '1894176896:AAFnuMzEb1yneKX4TAr0wbtYg3ovE0c0M4Q'

bot = telebot.TeleBot(TOKEN)

apihelper.proxy = {
    'https': 'socks5://5.133.198.165:24382'
}

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

# try:
bot.polling(none_stop=True)
# except Exception:
#     pass