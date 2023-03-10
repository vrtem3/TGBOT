import os
import telebot
import json
import requests
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token")

bot: TeleBot = telebot.TeleBot(TOKEN)


# AdvancedCustomFilter is for list, string filter values
class MainFilter(telebot.custom_filters.AdvancedCustomFilter):
    key = 'text'
    @staticmethod
    def check(message, text):
        return message.text in text


# Обрабатываются команды '/start' or '/help'
@bot.message_handler(commands=['start', 'help'], )
def start_help(message: telebot.types.Message):
    text = f"{message.chat.username}, hello"
    bot.reply_to(message, text)


# Обрабатываются сообщения 'start' or 'help'
@bot.message_handler(text=['start', 'help'])
def welcome_hi(message):
    text = f"{message.chat.username}, hello"
    bot.reply_to(message, text)


# Регистрируем кастомные фильтры
bot.add_custom_filter(MainFilter())


bot.polling(none_stop=True)
