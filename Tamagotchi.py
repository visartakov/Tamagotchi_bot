# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper
from SQLighter import SQLighter

apihelper.proxy = {'https':'socks5://98.162.25.29:31679'}
#apihelper.proxy = {'https':'socks5://45.33.71.52:27157'}


token = '569035913:AAE_mIGzN8KcLsr-snxXEFaVObU_Q6OQGfA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    db_worker = SQLighter('mybase.db')
    row = db_worker.select_all()
    bot.send_message(message.chat.id, row)
    db_worker.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)

"""commit1"""