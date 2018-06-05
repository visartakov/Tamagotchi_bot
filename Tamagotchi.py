# -*- coding: utf-8 -*-
import time
import telebot
from telebot import apihelper

apihelper.proxy = {'https':'socks5://98.162.25.29:31679'}

token = '569035913:AAE_mIGzN8KcLsr-snxXEFaVObU_Q6OQGfA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Привет. Как меня зовут?')


if __name__ == '__main__':
    bot.polling(none_stop=True)
