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

emoji = ['โค', '๐', '๐', '๐', '๐งก', '๐ค']

a = 0.1
flag = 1

def magic(message, flag):
    while True:
        if flag == 1:
            k = bot.send_message(message.chat.id, '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐๐๐ค๐๐๐ค๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐ค๐๐๐๐๐๐ค๐ค\n๐ค๐ค๐ค๐๐๐๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
            flag = 0
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐๐๐ค๐๐๐ค๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐ค๐๐๐๐๐๐ค๐ค\n๐ค๐ค๐ค๐๐๐๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐๐๐ค๐๐๐ค๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐ค๐๐๐๐๐๐ค๐ค\n๐ค๐ค๐ค๐๐๐๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐๐๐ค๐๐๐ค๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐๐๐๐๐๐๐๐ค\n๐ค๐ค๐๐๐๐๐๐ค๐ค\n๐ค๐ค๐ค๐๐๐๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐งก๐งก๐ค๐งก๐งก๐ค๐ค\n๐ค๐งก๐งก๐งก๐งก๐งก๐งก๐งก๐ค\n๐ค๐งก๐งก๐งก๐งก๐งก๐งก๐งก๐ค\n๐ค๐ค๐งก๐งก๐งก๐งก๐งก๐ค๐ค\n๐ค๐ค๐ค๐งก๐งก๐งก๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐งก๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        time.sleep(a)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐คโคโค๐คโคโค๐ค๐ค\n๐คโคโคโคโคโคโคโค๐ค\n๐คโคโคโคโคโคโคโค๐ค\n๐ค๐คโคโคโคโคโค๐ค๐ค\n๐ค๐ค๐คโคโคโค๐ค๐ค๐ค\n๐ค๐ค๐ค๐คโค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค')
        l = '๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค\n๐ค๐คโคโค๐คโคโค๐ค๐ค\n๐คโคโคโคโคโคโคโค๐ค\n๐คโคโคโคโคโคโคโค๐ค\n๐ค๐คโคโคโคโคโค๐ค๐ค\n๐ค๐ค๐คโคโคโค๐ค๐ค๐ค\n๐ค๐ค๐ค๐คโค๐ค๐ค๐ค๐ค\n๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค'
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
            l = l.replace('๐ค','โค', 1)
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = l)

        
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค\nโคโคโคโคโคโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโคโคโคโคโค\nโคโคโคโคโคโคโค\nโคโคโคโคโคโคโค\nโคโคโคโคโคโคโค\nโคโคโคโคโคโคโค\nโคโคโคโคโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโคโคโคโค\nโคโคโคโคโคโค\nโคโคโคโคโคโค\nโคโคโคโคโคโค\nโคโคโคโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโคโคโค\nโคโคโคโคโค\nโคโคโคโคโค\nโคโคโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโคโค\nโคโคโคโค\nโคโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโคโค\nโคโคโค')
        time.sleep(0.05)
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = 'โคโค')

        for_sleep = 0.05
        word = 'ะปัะฑะพะฒัั'
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
        name = 'ะะฒะฐะฝ'
        for i in range(len(name)):
            love = love + name[i]
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
            time.sleep(for_sleep)
        love = love + ' '
        lastname = 'ะะตะฑะตะดะตะฒ'
        for i in range(len(lastname)):
            love = love + lastname[i]
            bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
            time.sleep(for_sleep)
        time.sleep(for_sleep)
        love = love + 'โค'
        bot.edit_message_text(chat_id = message.chat.id, message_id = k.message_id , text = love)
        break




@bot.message_handler(commands=['help'])
def start_help(message):
    bot.send_message(message.chat.id, 'ะฏ ะผะพะณั ะฟะพะบะฐะทะฐัั ะดะตะฝั ะฝะตะดะตะปะธ, ััะพะฑั ัะตะฑะต ะฑัะปะพ ะปะตะณัะต ััะธัััั ะธ ะฝะต ะฟัะพัะฟะฐัั ะฟะฐัั\nะ ัะฐะบะถะต ั ะผะพะณั ะฟะพะบะฐะทะฐัั ะบะฐะบะฐั ัะตะนัะฐั ะฝะตะดะตะปั, ััะพะฑั ัั ััะฟะตะป ะฒัะต ะฒะพะฒัะตะผั ัะดะฐัั!'
        '\nะัั ั ะผะพะณั ะฟะพะดะฑัะพัะธัั ะบัะฑะธะบ ะธะปะธ ัะณะตะฝะตัะธัะพะฒะฐัั ัะตะฑะต ัะฐะฝะดะพะผะฝะพะต ัะธัะปะพ\n\nะัะต ััะพ ัั ะผะพะถะตัั ัะฒะธะดะตัั ะฒ \n/menu ะธะปะธ /day\nะ ััะพะฑั ัะฒะธะดะตัั ะผะฐะณะธั, ะฟะตัะตัะพะดะธ ะฟะพ \n/magic')



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.row("/magic", "/menu", "/day", "/help")
    bot.send_message(message.chat.id, 'ะะดัะฐะฒััะฒัะนัะต! ะงะตะณะพ ะถะตะปะฐะตัะต?', reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('๐ ะ?ะฐะฝะดะพะผะฝะพะต ัะธัะปะพ')
    item2 = types.KeyboardButton('๐ฒ ะะพะดะฑัะพัะธัั ะบัะฑะธะบ')
    item3 = types.KeyboardButton('ะะฐะทะฐะด')
    keyboard1.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'ะงัะพ ัะพัะธัะต?', reply_markup=keyboard1)

@bot.message_handler(commands=['day'])
def day(message):
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('ะะตะฝั ะฝะตะดะตะปะธ')
    item2 = types.KeyboardButton('ะะฐะบะฐั ัะตะนัะฐั ะฝะตะดะตะปั')
    item3 = types.KeyboardButton('ะะฐะทะฐะด')
    keyboard2.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'ะงัะพ ัะพัะธัะต?', reply_markup=keyboard2)

@bot.message_handler(commands=['magic'])
def magic1(message):
    magic(message, flag)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "ัะพัั":
        bot.send_message(message.chat.id, 'ะขะพะณะดะฐ ัะตะฑะต ััะดะฐ โ https://mtuci.ru/')
        bot.send_message(message.chat.id, 'ะงัะพ-ะฝะธะฑัะดั ะตัะต?', reply_markup=keyboard0)
    elif message.text.lower() == "๐ ัะฐะฝะดะพะผะฝะพะต ัะธัะปะพ":
        bot.send_message(message.chat.id, str(randint(0,100)))
    elif message.text.lower() == "๐ฒ ะฟะพะดะฑัะพัะธัั ะบัะฑะธะบ":
        bot.send_message(message.chat.id, 'ะะฐ ะบัะฑะธะบะต ะฒัะฟะฐะปะพ - ' + str(randint(1,6)) + ' ๐ฒ')
    elif message.text.lower() == "ะดะตะฝั ะฝะตะดะตะปะธ":
        bot.send_message(message.chat.id, str(day1))
    elif message.text.lower() == "ะบะฐะบะฐั ัะตะนัะฐั ะฝะตะดะตะปั":
        bot.send_message(message.chat.id, str(nums - 4))
    elif message.text.lower() == "ะฝะฐะทะฐะด":
        bot.send_message(message.chat.id, 'ะงัะพ ัะพัะธัะต?', reply_markup=keyboard0)
    else: 
        bot.send_message(message.chat.id, 'ะฏ ะฒะฐั ะฝะต ะฟะพะฝะธะผะฐั')


bot.polling(non_stop = True, interval = 0)