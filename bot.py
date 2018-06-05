# -*- coding: utf-8 -*-
import time
import telebot
from telebot import apihelper

apihelper.proxy = {'https':'socks5://98.162.25.29:31679'}

token = '569035913:AAE_mIGzN8KcLsr-snxXEFaVObU_Q6OQGfA'
bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
