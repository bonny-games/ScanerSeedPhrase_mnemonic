import time

import telebot

token = "5693782301:AAFATtbabMNJRTfFCWyK73KkkIE8r4kuhZc"
idChat = -945892436
bot = telebot.TeleBot(token)

# @bot.message_handler(content_types=['text', 'audio', 'video', 'photo', 'document'])
# def ObrobsicComand(message: telebot.types.Message):
#     print(message.chat.id)
# print("s")
# bot.polling(none_stop=True)


def mes(txt):
    print(txt)
    try:
        bot.send_message(idChat, txt)
    except:
        pass

