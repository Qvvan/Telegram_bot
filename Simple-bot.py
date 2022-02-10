import telebot
from telebot import types
from random import randint
from datetime import datetime , date
import calendar
import time

token = "5278804872:AAHKD4HyQhwt9FBMb_GpX005_fwdva1A3qs"
bot = telebot.TeleBot(token)

my_date = date.today()
day1 = calendar.day_name[my_date.weekday()]
nums = int(datetime.utcnow().isocalendar()[1])

keyboard0 = types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard0.row("/magic", "/menu", "/day","/help")

emoji = ['❤', '💛', '💜', '💙', '🧡', '🤎']

a = 0.1
flag = 1

def magic(message, flag):
    while True:
        if flag == 1:
            k = bot.send_message(message.chat.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
            flag = 0
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤎🤎🤍🤎🤎🤍🤍\n🤍🤎🤎🤎🤎🤎🤎🤎🤍\n🤍🤎🤎🤎🤎🤎🤎🤎🤍\n🤍🤍🤎🤎🤎🤎🤎🤍🤍\n🤍🤍🤍🤎🤎🤎🤍🤍🤍\n🤍🤍🤍🤍🤎🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤❤🤍❤❤🤍🤍\n🤍❤❤❤❤❤❤❤🤍\n🤍❤❤❤❤❤❤❤🤍\n🤍🤍❤❤❤❤❤🤍🤍\n🤍🤍🤍❤❤❤🤍🤍🤍\n🤍🤍🤍🤍❤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
        l = '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤❤🤍❤❤🤍🤍\n🤍❤❤❤❤❤❤❤🤍\n🤍❤❤❤❤❤❤❤🤍\n🤍🤍❤❤❤❤❤🤍🤍\n🤍🤍🤍❤❤❤🤍🤍🤍\n🤍🤍🤍🤍❤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍'
        lol = list(l)
        time.sleep(a)
        for i in range(20):
            lol[12], lol[13], lol[15], lol[16] = [emoji[randint(0,5)] for i in range(4)]
            lol[21], lol[22], lol[23], lol[24], lol[25], lol[26], lol[27] = [emoji[randint(0,5)] for i in range(7)]
            lol[31], lol[32], lol[33], lol[34], lol[35], lol[36], lol[37] = [emoji[randint(0,5)] for i in range(7)]
            lol[42], lol[43], lol[44], lol[45], lol[46] = [emoji[randint(0,5)] for i in range(5)]
            lol[53], lol[54], lol[55] = [emoji[randint(0,5)] for i in range(3)]
            lol[64] = emoji[randint(0,5)]
            string = "".join(lol)
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = string)
            time.sleep(0.1)

        for i in range(45):
            l = l.replace('🤍','❤', 1)
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = l)

        
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤\n❤❤❤❤❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤❤❤❤\n❤❤❤❤❤❤\n❤❤❤❤❤❤\n❤❤❤❤❤❤\n❤❤❤❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤❤❤\n❤❤❤❤❤\n❤❤❤❤❤\n❤❤❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤❤\n❤❤❤❤\n❤❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤❤\n❤❤❤')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '❤❤')

        for_sleep = 0.05
        word = 'любовью'
        love = 'C '
        for i in range(len(word)):
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
            love = love + word[i]
            time.sleep(for_sleep)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
        time.sleep(for_sleep)
        love = love + ', '
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
        time.sleep(for_sleep)
        name = 'Иван'
        for i in range(len(name)):
            love = love + name[i]
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
            time.sleep(for_sleep)
        love = love + ' '
        lastname = 'Лебедев'
        for i in range(len(lastname)):
            love = love + lastname[i]
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
            time.sleep(for_sleep)
        time.sleep(for_sleep)
        love = love + '❤'
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
        break




@bot.message_handler(commands=['help'])
def start_help(message):
    bot.send_message(message.chat.id, 'Я могу показать день недели, чтобы тебе было легче учиться и не проспать пару\nА также я могу показать какая сейчас неделя, чтобы ты успел все вовремя сдать!'
        '\nЕщё я могу подбросить кубик или сгенерировать тебе рандомное число\n\nВсе это ты можешь увидеть в \n/menu или /day\nА чтобы увидеть магию, переходи по \n/magic')



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.row("/magic", "/menu", "/day", "/help")
    bot.send_message(message.chat.id, 'Здравствуйте! Чего желаете?', reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎈 Рандомное число')
    item2 = types.KeyboardButton('🎲 Подбросить кубик')
    item3 = types.KeyboardButton('Назад')
    keyboard1.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Что хотите?', reply_markup=keyboard1)

@bot.message_handler(commands=['day'])
def day(message):
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('День недели')
    item2 = types.KeyboardButton('Какая сейчас неделя')
    item3 = types.KeyboardButton('Назад')
    keyboard2.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Что хотите?', reply_markup=keyboard2)

@bot.message_handler(commands=['magic'])
def magic1(message):
    magic(message, flag)

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