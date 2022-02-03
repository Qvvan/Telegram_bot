import telebot
from telebot import types
from random import randint
from datetime import datetime , date
import calendar

token = "5278804872:AAHKD4HyQhwt9FBMb_GpX005_fwdva1A3qs"
bot = telebot.TeleBot(token)

my_date = date.today()
day1 = calendar.day_name[my_date.weekday()]
nums = int(datetime.utcnow().isocalendar()[1])

keyboard0 = types.ReplyKeyboardMarkup()
keyboard0.row("/menu", "/day")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/menu", "/day")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def start(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎈 Рандомное число')
    item2 = types.KeyboardButton('🎲 Подбросить кубик')
    item3 = types.KeyboardButton('Назад')
    keyboard1.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Что хотите?', reply_markup=keyboard1)

@bot.message_handler(commands=['day'])
def start(message):
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('День недели')
    item2 = types.KeyboardButton('Какая сейчас неделя')
    item3 = types.KeyboardButton('Назад')
    keyboard2.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Что хотите?', reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
        bot.send_message(message.chat.id, 'Что-нибудь еще?', reply_markup=keyboard0)
    elif message.text.lower() == "🎈 рандомное число":
        bot.send_message(message.chat.id, str(randint(0,100)))
    elif message.text.lower() == "🎲 подбросить кубик":
        bot.send_message(message.chat.id, 'На кубике выпало - ' + str(randint(1,6)) + ' 🎲')
    elif message.text.lower() == "день недели":
        bot.send_message(message.chat.id, str(day1))
    elif message.text.lower() == "какая сейчас неделя":
        bot.send_message(message.chat.id, str(nums - 4))
    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, 'Что хотите?', reply_markup=keyboard0)
    else: 
        bot.send_message(message.chat.id, 'Я вас не понимаю')


bot.polling(non_stop = True, interval = 0)
