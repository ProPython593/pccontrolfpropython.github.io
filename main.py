import telebot
import os
import subprocess
from telebot import types # для указание типов
import pyautogui

bot = telebot.TeleBot('6156359786:AAGuDkihO-Orb19CKQNcVmJM8ZR-Vb9Ym38')
ownerid = "6037918044"


@bot.message_handler(commands=['start'])
def start(message):
    global ownerid
    if message.from_user.id==6037918044 or message.from_user.id==5926772909:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выключить!")
        btn2 = types.KeyboardButton("Перезагрузить!")
        btn3 = types.KeyboardButton("Помошь")
        btn4 = types.KeyboardButton("Отправить скриншот")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! я бот для управления пк.".format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Вы не OWNER")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global ownerid
    if message.from_user.id==6037918044 or message.from_user.id==5926772909:
        if message.text == "Выключить!":  
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='shutdown') #кнопка «Да»
            keyboard.add(key_yes) #добавляем кнопку в клавиатуру
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no)  
            key_undo = types.InlineKeyboardButton(text='Отменить задачу', callback_data='undo')
            keyboard.add(key_undo) #добавляем кнопку в клавиатуру 
            bot.send_message(message.from_user.id, "Вы уверены?", reply_markup=keyboard)
        elif message.text == "Помошь": 
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Мой ютуб канал", url='https://www.youtube.com/channel/UCfQ5rjChy6giJOlcv814cfQ')
            btn2 = types.InlineKeyboardButton("Мой сайт", url='https://propython593.github.io')
            btn3 = types.InlineKeyboardButton("проект на GitHub", url='https://github.com/ProPython593/pccontrolfpropython.github.io/')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, "Привет я бот от ProPython593(Также извесный как ProPythonYT) предназначен для управления пк, Я пока умею только выключать и перезагружать(не стабильно), а также отправлять скриншот экрана. Надеюсь меня обновят и добавят новых функций. Внизу есть ссылки на проект и на propython:", reply_markup=markup)
        elif message.text == "Перезагрузить!":  
            keyboard = types.InlineKeyboardMarkup() #наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='reboot') #кнопка «Да»
            keyboard.add(key_yes) #добавляем кнопку в клавиатуру
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no) 
            key_undo = types.InlineKeyboardButton(text='Отменить задачу', callback_data='undo')
            keyboard.add(key_undo) #добавляем кнопку в клавиатуру 
            bot.send_message(message.from_user.id, "Вы уверены?", reply_markup=keyboard)
        elif message.text == "Отправить скриншот":  
            bot.send_message(message.from_user.id, "Отправляю")
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\User\Desktop\ds bot\time files\screen.png')
            bot.send_document(message.chat.id, open(r'C:\Users\User\Desktop\ds bot\time files\screen.png', 'rb'))
            os.remove(r'C:\Users\User\Desktop\ds bot\time files\screen.png')
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю.")
    else:
        bot.send_message(message.chat.id, text="Вы не OWNER")
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "shutdown": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Выключаю')
        os.system("shutdown /s /f")
    elif call.data == "reboot": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Перезагружаю')
        os.system("shutdown /r")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Возвращаюсь')
    elif call.data == "undo":
        bot.send_message(call.message.chat.id, 'Выключение/Перезагрузка отменена')
        os.system("shutdown -a")
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Обратиться", url='https://forms.gle/YikJbts53cjRxT1e9')
        markup.add(btn1)
        bot.send_message(call.message.chat.id, 'Не верный callback ' + call.data + ' Обратитесь к ProPython', reply_markup=markup)
bot.polling(none_stop=True, interval=0)
