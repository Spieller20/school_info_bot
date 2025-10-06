# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types 
from telebot.types import InputMediaPhoto
from dotenv import load_dotenv
from pathlib import Path
import random
import sqlite3
import os


env_path = Path(__file__).parent / 'School_Bot.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv("BOT_TOKEN") # создание бота

bot = TeleBot(token=TOKEN)

# обработчик команды '/start': главное меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Инвентарь к учебному году")
    btn2 = types.KeyboardButton("Домашние задания")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Приветствую, {0.first_name}! Добро пожаловать в информатор музыкального отделения Детской школы искусств №7!\nЗдесь вы можете узнать  что нужно к новому учебному году про предметам 'Сольфеджио' и 'Слушание музыки/Музыкальная литература'\nПо этим же предметам тут вы сможете узнать все текущие домашние задания, существующие на сегодняшний день".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="О чём Вы хотите узнать?".format(message.from_user))
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDd3MjJ2MDE3MjNqZzdvbTNxc2R6a2Qzc28xZHN2MHAyOXF0czQ1ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Qw2g4Tef2HZXpffWFP/giphy.gif', None, 'Text')
  
# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Инвентарь к учебному году"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("1 класс")
     btn2 = types.KeyboardButton("2 класс")
     btn3 = types.KeyboardButton("3 класс")
     btn4 = types.KeyboardButton("4 класс")
     btn5 = types.KeyboardButton("5 класс")
     btn6 = types.KeyboardButton("6 класс")
     btn7 = types.KeyboardButton("7 класс")
     btn8 = types.KeyboardButton("8 класс")
     btn9 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
     bot.send_message(message.chat.id,"В каком классе учитесь?", reply_markup=markup)
         

    #Рекомендации по классам
    elif(message.text == "1 класс"):
     chat_id = message.chat.id    
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/ElF8PLhW9Jp_NA'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/C19cGMXcnKOtMA'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 1 класса:</i></b>\n\n' # Дневник
        '<b><i>1)Учебник: </i></b>авторы - Н.Баева, Т.Зебряк "Сольфеджио для 1-2 классов".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 1 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
              ]
     bot.send_media_group(chat_id, INVENTAR)

    elif(message.text == "2 класс"):
     chat_id = message.chat.id    
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/ElF8PLhW9Jp_NA'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/qUqcqgDeM2aioQ'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 2 класса:</i></b>\n\n' # Дневник
        '<b><i>1)Учебник: </i></b>авторы - Н.Баева, Т.Зебряк "Сольфеджио для 1-2 классов".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 2 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)

     
    elif(message.text == "3 класс"):
     chat_id = message.chat.id
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto('https://disk.yandex.ru/i/9cmUPg8NAFD7GA'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 3 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 3 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)

     
    elif(message.text == "4 класс"):
     chat_id = message.chat.id  
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto('https://disk.yandex.ru/i/gUtoZ2J8LBxenQ'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 4 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 4 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)

     
    elif(message.text == "5 класс"):
     chat_id = message.chat.id 
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto('https://disk.yandex.ru/i/G2LitWGXt4BqCg'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 5 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 5 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)
     

    elif(message.text == "6 класс"):
     chat_id = message.chat.id
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto('https://disk.yandex.ru/i/OqmA8pv9LmRRoQ'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 6 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 6 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)
     

    elif(message.text == "7 класс"):
     chat_id = message.chat.id
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto('https://disk.yandex.ru/i/Hb8DQH6XRIjLmQ'), #Рабочая тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 7 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>автор - Г.Ф.Калинина "Сольфеджио, 7 класс".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)

     
    elif(message.text == "8 класс"):
     chat_id = message.chat.id 
     INVENTAR = [
        InputMediaPhoto('https://disk.yandex.ru/i/XZCuvpZQ9y6gXg'), #Учебник
        InputMediaPhoto('https://disk.yandex.ru/i/3pE6ViMr1kThoQ'),
        InputMediaPhoto("https://disk.yandex.ru/i/_zfruSyHRC34-g"),
        InputMediaPhoto("https://disk.yandex.ru/i/sEp_ap3QSNpSGw"),
        InputMediaPhoto("https://disk.yandex.ru/i/va6nijhtBqIrzA"), # Нотная тетрадь
        InputMediaPhoto("https://disk.yandex.ru/i/rtSef9ej6ZvpPA"),
        InputMediaPhoto("https://disk.yandex.ru/i/0lxTat-OcBOkCg"),
        InputMediaPhoto("https://disk.yandex.ru/i/0HEgwFZssbAGYQ", caption='<b><i>Необходимый инвентарь для 8 класса:</i></b>\n\n' # Дневник
        '<b><i>Учебник: </i></b>авторы - Б.Калмыков, Г.Фридкин. Приобрести можно любой из показанных примеров.".\n\n' 
        '<b><i>2)Рабочая тетрадь: </i></b>в 8 классе рабочая тетрадь <b>не нужна</b>".\n\n' 
        '<b><i>3)Нотная тетрадь: </i></b> это чистая тетрадь для записи нот (примеры на фото).\n\n'
        '<b><i>4)Дневник для музыкальной школы: </i></b>он приобретается один на все предметы. Просьба не путать с дневниками для общеобразовательных школ. Они отличаются по наполнению (примеры дневников на фото).\n\n' 
        '<b><i>5)Канцелярские принадлежности:</i></b> ручка, карандаш, ластик, точилка\n\n' 
        'Просим внимательно ознакомиться с примерами на фото. Инвентарь можно приобрести либо в книжных магазинах, либо на маркетплейсах.', parse_mode='HTML')
            ]
     bot.send_media_group(chat_id, INVENTAR)

     
    #Меню "Домашние задания"
    elif(message.text == "Домашние задания"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Сентябрь")
     btn2 = types.KeyboardButton("Октябрь")
     btn3 = types.KeyboardButton("Ноябрь")
     btn4 = types.KeyboardButton("Декабрь")
     btn5 = types.KeyboardButton("Январь")
     btn6 = types.KeyboardButton("Февраль")
     btn7 = types.KeyboardButton("Март")
     btn8 = types.KeyboardButton("Апрель")
     btn9 = types.KeyboardButton("Май")
     btn10 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
     bot.send_message(message.chat.id,text="Выберите месяц урока", reply_markup=markup)

    #Меню выбранного месяца
    elif(message.text == "Сентябрь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("6, 8 сентября 2025")
     btn2 = types.KeyboardButton("13, 15 сентября 2025")
     btn3 = types.KeyboardButton("20, 22 сентября 2025")
     btn4 = types.KeyboardButton("27, 29 сентября 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Октябрь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("4, 6 октября 2025")
     btn2 = types.KeyboardButton("11, 13 октября 2025")
     btn3 = types.KeyboardButton("18, 20 октября 2025")
     btn4 = types.KeyboardButton("25, 27 октября 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Ноябрь(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("1, 3 ноября 2025")
     btn2 = types.KeyboardButton("8, 10 ноября 2025")
     btn3 = types.KeyboardButton("15, 17 ноября 2025")
     btn4 = types.KeyboardButton("22, 24 ноября 2025")
     btn5 = types.KeyboardButton("29 ноября, 1 декабря 2025")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Декабрь(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("6, 8 декабря 2025")
     btn2 = types.KeyboardButton("13, 15 декабря 2025")
     btn3 = types.KeyboardButton("20, 22 декабря 2025")
     btn4 = types.KeyboardButton("27, 29 декабря 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Январь(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("3, 5 января 2026")
     btn2 = types.KeyboardButton("10, 12 января 2026")
     btn3 = types.KeyboardButton("17, 19 января 2026")
     btn4 = types.KeyboardButton("24, 26 января 2026")
     btn5 = types.KeyboardButton("31 января, 2 февраля 2026")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup) 

    elif(message.text == "Февраль(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("7, 9 февраля 2026")
     btn2 = types.KeyboardButton("14, 16 февраля 2026")
     btn3 = types.KeyboardButton("21, 23 февраля 2026")
     btn4 = types.KeyboardButton("28 февраля, 2 марта 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Март(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("7, 9 марта 2026")
     btn2 = types.KeyboardButton("14, 16 марта 2026")
     btn3 = types.KeyboardButton("21, 23 марта 2026")
     btn4 = types.KeyboardButton("28, 30 марта 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Апрель(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("4, 6 апреля 2026")
     btn2 = types.KeyboardButton("11, 13 апреля 2026")
     btn3 = types.KeyboardButton("18, 20 апреля 2026")
     btn4 = types.KeyboardButton("25, 27 апреля 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Май(locked)"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("2, 4 мая 2026")
     btn2 = types.KeyboardButton("9, 11 мая 2026")
     btn3 = types.KeyboardButton("16, 18 мая 2026")
     btn4 = types.KeyboardButton("23, 25 мая 2026")
     btn5 = types.KeyboardButton("30 мая 2026")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)  

    
    #Меню выбранной даты урока
    elif(message.text == "6, 8 сентября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Научиться писать скрипичный ключ либо в нотной тетради, либо в рабочей тетради на стр. 4\n\n"
                      "<b><i>Слушание музыки:</i></b> Шорникова «Музыкальная литература» 1 год Введение «Музыка и мы», ответить на вопросы устно\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Р.т. С. 17 номер 11\n\n"
                      "<b><i>Слушание музыки:</i></b> Учебник: Царёва « Уроки госпожи Мелодии» 2 кл. Выучить слова в тетради\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 7 До мажор сделать по образцу\n\n"
                      "<b><i>Слушание музыки:</i></b> Шорникова «Музыкальная литература» 2 год Урок 1, стр. 4-6, ответить на вопросы устно\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> 4 класс Р.т. С. 7 номер 11 сделать в скрипичном ключе\n\n"
                      "<b><i>Музыкальная литература:</i></b> Шорникова «Музыкальная литература» 1 год Введение «Музыка и мы», ответить на вопросы устно\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> учебник Калмыков, Фридкин 1 часть, номер 275 выучить наизусть"
                      "\n\n<b><i>Музыкальная литература:</i></b> Учебник: Шорникова «Музыкальная литература» 2 год обучения Урок 1, стр.4-6, ответить на вопросы устно\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Учебник: Шорникова « Музыкальная литература» 2 год Повторить уроки 1-20\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Учебник: Шорникова «Музыкальная литература» 3 год Урок 35, ответить на вопросы 1-10 письменно\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

    elif(message.text == "13, 15 сентября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Научиться писать нотку «до» первой октавы в нотной тетради. Для знающих ноты смотреть сообщение с картинкой.\n\n"
                      "<b><i>Слушание музыки:</i></b> Уроки 2-3, стр 11-16\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> р.т. с. 6 номера 1, 2 ( на с.3. в этой же тетради есть все подсказки: что такое устойчивые и неустойчивые ступени, как подписывать римские цифры и т.д.)\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 22 1 кл.знать инструменты симфонического оркестра\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> р.т. с. 7 по образцу сделать соль мажор\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 2, вопросы стр 10 письменно\n\n" 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> р.т. с 7 номер 9 (весь) + подписать ступеньки римскими цифрами\n\n"
                      "<b><i>Музыкальная литература:</i></b> Уроки 2-3, стр 11-16\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> учебник Калмыков-Фридкин (одноголосие) номер 275. Первое предложение (первые 4 такта) – записать в увеличении, т.е. каждая длительность увеличивается вдвое (восьмушка стала четвертью, четверть – половинкой и т.д.). Размер 4/4. Второе предложение (5-8 такты) записать в уменьшении. Размер 2/8. Дальше не надо."
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 2, письменно ответить на вопросы стр 10\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой."
                      "\n\n<b><i>Музыкальная литература:</i></b> Повторить уроки 8-11, урок 21, письменно ответить на вопросы после 21 урока\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 35, письменно ответить на вопросы 1-19\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                        parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/iAJKmwZ1Q0lEJA', caption='Задание для 1 класса для тех, кто ноты знает. Прохлопать ритмические рисунки. сначала каждую строчку отдельно, затем попробовать двумя руками (например, 1 строчка - правая рука, 2 строчка - левая.) можно распечатать и разрезать ритмы по строчкам и комбинировать разные варианты ритмических партитур.' )
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/sVil6IJdZX1oXg', caption='<b><i>6, 7 классы –</i><b> пользуясь буквенными обозначениями подписать аккорды в гармонии', parse_mode='HTML')
     bot.send_message(message.chat.id, 'Дополнение (для всех классов): обязательно хлопаем со счётом вслух. Не молчим. Раз и 2 и 3 и 4 и')
        
    elif(message.text == "20, 22 сентября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио (утренняя и вечерняя группа):</i></b> прописать в тетради ноту 'ре'\n\n"
                      "<b><i>Слушание музыки:</i></b> уроки 2-3, письменно ответить на вопросы стр 20\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> выучить строение минорной гаммы (р.т. С. 3 есть подсказка), построить в тетради гамму ля минор\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> р.т с. 10 буква Д, транспонировать в си бемоль мажор\n\n"
                      "<b><i>Слушание музыки:</i></b> Введение стр 3-5 или 5-7 ( разные издания учебника) до знака кассеты или диска. Вспомнить сказку А.С. Пушкина «Золотой петушок»\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> учебник Калмыков фридкин номер 182 петь с тактированием с названием нот\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> учебник Калмыков Фридкин номера 83,85 петь с тактированием и  названием нот\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 3-4 биография Баха в таблице\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> учебник Калмыков фридкин номер 182 петь с тактированием с названием нот\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> учебник Калмыков Фридкин номера 83,85 петь с тактированием и  названием нот\n\n"
                      "<b><i>Музыкальная литература:</i></b> уроки 2-3, письменно ответить на вопросы стр 20\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 3-4 биография Баха в таблице\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 22, биография Шуберта в таблице, письменно ответить на вопросы стр 173\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> 6,7 класс - задание прежнее"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 14, письменно ответить на вопросы\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/zohfANwSMnYnlQ', caption='<b><i>5,6 класс -</i></b> Крылатые качели петь с тактированием и названием нот', parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/zj8SKEdwAv5f7g', caption='<b><i>1 кл. внебюджет, сольфеджио (7-9 лет) -</i></b> раскрасить рисунок', parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/UZT1IwQBaXjASA', caption='<b><i>1 кл. внебюджет, сольфеджио (10-14 лет) -</i></b> расставить тактовые чёрточки', parse_mode='HTML')

    elif(message.text == "27, 29 сентября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"                      
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Р.т. С. 15 номера 20,21\n\n"
                      "<b><i>Слушание музыки:</i></b> стр 20, письменно ответить на вопросы. Урок 4 прочитать\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 12 номера 10,11\n\n"
                      "<b><i>Слушание музыки:</i></b> Введение, выучить определение музыкального образа и истоки музыкального образа\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n1) Рт. С. 7 фа мажор, с. 8 ре мажор (все сделать по образцу) \n2) учебник калмыков фридкин 1 часть, номер 181 разобрать (ритм и ноты)\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 5 прочитать, письменно ответить на вопросы стр 26\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n1) рт. С. 8 номер 12 \n2) учебник калмыков фридкин 1 часть, номер 181 разобрать (ритм и ноты)\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 4, письменно ответить на вопросы стр 20\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> рт. С. 6 номера 1,2,3,4"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 5, письменно ответить на вопросы стр 26\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 23 стр.174-178, письменно ответить на вопросы стр 173\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 14, письменно ответить на вопросы стр 136\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/C-G_7LJ4x_q6ow', caption='<b><i>6 и 7 классы:</i></b> диктант транспонировать в Тональность с 3 знаками (на выбор - либо ля мажор, либо ми бемоль мажор)', parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/vDeoyZpoboVpdQ', caption='<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b> нарисовать музыкальную лесенку (на фото примеры того, как она может выглядеть), подписать ступеньки (как в классе)', parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b> Построить в тетради от до, ми, соль, си полутон вверх. \nОт нот ре, фа, ля построить тон вверх", parse_mode='HTML')   

    elif(message.text == "4, 6 октября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 6 номера 2,3 \nНа следующий урок принести цветные карандаши\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 4, письменно ответить на вопросы стр 25\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 13 номер 4, с. 17 номер 9\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 1, прочитать. Выучить определение музыкального образа и его истоки.\nЗадание 1, О рыцарях, любви, добре и зле.\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в тетради любую мажорую Тональность и одноименную минорную. Обвести 3,6,7 ступени\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 6, письменно ответить на вопросы стр 40\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в тетради любую мажорую Тональность и одноименную минорную. Обвести 3,6,7 ступени\n\n"
                      "<b><i>Музыкальная литература:</i></b> урок 4, письменно ответить на вопросы стр 25\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 7 номера 7,8,9,10"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 6, письменно ответить на вопросы стр 40\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 6 номера 1,2 \nУчебник калмыков фридкин номер 401 петь с тактированием"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 23, письменно ответить на вопросы стр 182\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 6 номера 1,2 \nУчебник калмыков фридкин номер 401 петь с тактированием"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 15, таблица биографии Бородина\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b> \n1)рт. С. 15 номер 20,21 (доделать классную работу) \n2) рт. С. 6 номера 2,3 (раскрасить нотки)", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b> Учебник калмыков фридкин номера 169,170,172 выучить наизусть и петь с дирижированием", parse_mode='HTML')        

    elif(message.text == "(locked)11, 13 октября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "(locked)18, 20 октября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "(locked)25, 27 октября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "1, 3 ноября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "8, 10 ноября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "15, 17 ноября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "22, 24 ноября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "29 ноября, 1 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "6, 8 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "13, 15 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "20, 22 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "27, 29 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "3, 5 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "10, 12 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "17, 19 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "24, 26 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "31 января, 2 февраля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "7, 9 февраля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "14, 16 февраля 2026"):
     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "21, 23 февраля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "28 февраля, 2 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "7, 9 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "14, 16 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "21, 23 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "28, 30 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "4, 6 апреля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "11, 13 апреля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "18, 20 апреля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "25, 27 апреля 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "2, 4 мая 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "9, 11 мая 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "16, 18 мая 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "23, 25 мая 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    elif(message.text == "30 мая 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>2 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n "
                      
                      "<b><i>3 класс:</i></b>\nСольфеджио:\n"
                      "Слушание музыки:\n\n " 
                      
                      "<b><i>4 класс:</i></b>\nСольфеджио:\n"
                      "Музыкальная литература:\n\n"
                      
                      "<b><i>5 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>6 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>7 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n\n "
                      
                      "<b><i>8 класс:</i></b>\nСольфеджио:"
                      "\nМузыкальная литература:\n",
                         parse_mode='HTML')

    #Главное меню            
    elif (message.text == "Главное меню"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Инвентарь к учебному году")
     btn2 = types.KeyboardButton("Домашние задания")   
     markup.add(btn1, btn2)
     bot.send_message(message.chat.id, text="О чём Вы хотите узнать?", reply_markup=markup)
    else:
     bot.send_message(message.chat.id, text="Информация по запросу пока недоступна или запрос не соответствует логике сервиса.")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
