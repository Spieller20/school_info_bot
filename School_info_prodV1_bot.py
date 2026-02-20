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

    elif(message.text == "Ноябрь"):
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

    elif(message.text == "Январь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("3, 5 января 2026")
     btn2 = types.KeyboardButton("10, 12 января 2026")
     btn3 = types.KeyboardButton("17 января 2026")
     btn4 = types.KeyboardButton("24 января 2026")
     btn5 = types.KeyboardButton("31 января 2026")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup) 

    elif(message.text == "Февраль"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("7 февраля 2026")
     btn2 = types.KeyboardButton("14 февраля 2026")
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
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/sVil6IJdZX1oXg', caption='<b><i>6, 7 классы –</i></b> пользуясь буквенными обозначениями подписать аккорды в гармонии', parse_mode='HTML')
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

    elif(message.text == "11, 13 октября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 6 номера 1,4, 5\n\n"
                      "<b><i>Слушание музыки:</i></b> уроки 5-6, письменно ответить на вопросы стр 39\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 18 Номера 19,20\nС. 19 номера 21,22\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 2\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С 7 номер 1 фа мажор. Это к субботе 18.10\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 7, письменно ответить на вопросы стр 45\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> Построить как в классе гаммы До мажор-до минор, ми мажор-ми минор. Поднимать III, VI, VII ступени\nПостроить в тетради интервалы ч1. Ч4, ч5, ч8 от нот ре, ми\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> Рт с. 7 номер 7 1 строчка\nПостроить в тетради интервалы ч1. Ч4. Ч5.ч8 от нот ре, ми\n\n"
                      "<b><i>Музыкальная литература:</i></b> уроки 5-6, письменно ответить на вопросы стр 39\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт с. 11 №15 доделать"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 7, письменно ответить на вопросы стр 45\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. с. 9 №9"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 24, письменно ответить на вопросы стр 187\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. с. 27 №24"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 16, письменно ответить на вопросы стр 158\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\nрт. с. 9 номера 20, 21\n(+р.т. с. 6 номера 2,3 - старое задание для тех, кто не сделал)", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\nр.т. с. 19 номера 2,3.\nс. 20 номера 10,11\nс. 21 номер 18", parse_mode='HTML')

    elif(message.text == "18, 20 октября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 7, письменно ответить на вопросы стр 48\n\n"
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 3\n\n"
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)\n\n"
                      "<b><i>Слушание музыки:</i></b> уроки 2-7 повторить\n\n" 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)\n\n"
                      "<b><i>Музыкальная литература:</i></b> урок 7, письменно ответить на вопросы стр 48\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 2-7 повторить\n\n"
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 21-25 повторить\n\n"
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Последний урок (задания нет)"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 17-18, письменно ответить на вопросы стр 169\n\n"
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n ",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\nРт с 6 номера 1,4,5", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\nРт. С. 20 номер 7, с. 21 номер 15", parse_mode='HTML')

    elif(message.text == "25, 27 октября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет\n"
                      "<b><i>Музыкальная литература:</i></b> Задания нет\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n<b><i>Музыкальная литература:</i></b> Задания нет\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n<b><i>Музыкальная литература:</i></b> Задания нет\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n<b><i>Музыкальная литература:</i></b> Задания нет\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет"
                      "\n<b><i>Музыкальная литература:</i></b> Задания нет\n",
                         parse_mode='HTML')

    elif(message.text == "1, 3 ноября 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)\n"
                      "<b><i>Слушание музыки:</i></b> Каникулярный день (задания нет)\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)\n"
                      "<b><i>Слушание музыки:</i></b> Каникулярный день (задания нет)\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)\n"
                      "<b><i>Слушание музыки:</i></b> Каникулярный день (задания нет)\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)\n"
                      "<b><i>Музыкальная литература:</i></b> Каникулярный день (задания нет)\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)"
                      "\n<b><i>Музыкальная литература:</i></b> Каникулярный день (задания нет)\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)"
                      "\n<b><i>Музыкальная литература:</i></b> Каникулярный день (задания нет)\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)"
                      "\n<b><i>Музыкальная литература:</i></b> Каникулярный день (задания нет)\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Каникулярный день (задания нет)"
                      "\n<b><i>Музыкальная литература:</i></b> Каникулярный день (задания нет)\n",
                         parse_mode='HTML')

    elif(message.text == "8, 10 ноября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 25 номер 9 А, Б\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 8, письменно ответить на вопросы стр 56\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в нотной тетради все интервалы от ноты 'ми', раскрасить только чистые интервалы\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 3 «О том, как сделать музыку живой» повторить приемы развития\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задания нет\n\n"
                      "<b><i>Слушание музыки:</i></b> стр. 46-49, письменно ответить на вопросы стр 49\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> Построить в тетради мажорные трезвучия от нот ре ь, ми ь, соль ь, ля ь, си ь\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> Рт. С. 19 номера 1,2 3\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 8, письменно ответить на вопросы стр 56\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в нотной тетради Д7 с обращениями и разрешениями в тональности a-moll"
                      "\n\n<b><i>Музыкальная литература:</i></b> стр 46-49, письменно ответить на вопросы стр 49\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в нотной тетради Д7 с обращениями и разрешениями в любой мажорной тональности (кроме до мажора)"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 26, письменно ответить на вопросы стр 205\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Построить в нотной тетради Д7 с обращениями и разрешениями в любой мажорной тональности (кроме до мажора)"
                      "\n\n<b><i>Музыкальная литература:</i></b> Уроки 20-21 биография Мусоргского в таблице, письменно ответить на вопросы стр 185\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/ycGtKJRW44K6UQ', caption='<b><i>1 кл. внебюджет, сольфеджио (7-9 лет и 10-14 лет):</i></b> 1) учебник баева-зебряк, номер 52 петь \n2) Рт. С. 25 номер 6, номер 9 (а) только до мажор \nИ не забываем писать скрипичный ключ в начале строчки', parse_mode='HTML')

    elif(message.text == "15, 17 ноября 2025"):     
     bot.send_message(message.chat.id,

                      "<b>ВНИМАНИЕ</b>\n"
                      "Для обучающихся на платном отделении задано другое задание. Смотреть сообщения ниже (пометка 'внебюджет')\n\n"
                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 25 номер 6 (только первая строчка). Найти опевания + прохлопать ритм со счётом\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 9, письменно ответить на вопросы стр 65\n\n"
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> 1) рт. С. 18 номера 14,15\n2) рт. С. 19 номер 28 построить м6 и б6 от разных нот\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> Рт. С. 20 номер 32 (а)\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 5\n\n"
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Смотреть сообщение с картинкой\n\n"
                      "<b><i>Слушание музыки:</i></b> урок 8, письменно ответить на вопросы стр 60\n\n" 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио (утренняя группа):</i></b> Рт. С. 19 номера 1, 2, 3\n\n"
                      "<b><i>Сольфеджио (вечерняя группа):</i></b> Учебник калмыков фридкин, номер 188 первые две строчки записать в тетради в тональности ре минор.\n\n"
                      "<b><i>Музыкальная литература:</i></b> урок 9, письменно ответить на вопросы стр 65\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт с 22 номера 1, 2, 3"
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 8, письменно ответить на вопросы стр 60\n\n"
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 24 номер 10 только Б53 и м53 (утренняя группа)\nСлушать интервалы https://xn--80ahdkilbo1bvw1el.xn--p1ai/?ysclid=mi3ai29y77426224905 (вечерняя группа)"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 27-28, стр 206-210\n\n"
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Слушать интервалы https://xn--80ahdkilbo1bvw1el.xn--p1ai/?ysclid=mi3ai29y77426224905"
                      "\n\n<b><i>Музыкальная литература:</i></b> уроки 22-23, письменно ответить на вопросы стр 194\n\n"
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')
        
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/eua5GyUyaWOVzg', caption='<b><i>3 класс, сольфеджио:</i></b>\nСлушать интервалы в тренажёре.\nhttps://идеальныйслух.рф/\nНа фото инструкция', parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\nр.т. с. 25 номер 9 А и Б только до мажор", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\nПостроить в нотной тетради все интервалы от примы до октавы от ноты 'ми' (как в классе)", parse_mode='HTML')

    elif(message.text == "22, 24 ноября 2025(locked)"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "29 ноября, 1 декабря 2025(locked)"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "6, 8 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "13, 15 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "20, 22 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "27, 29 декабря 2025"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "3, 5 января 2026(locked)"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "10, 12 января 2026(locked)"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

    elif(message.text == "17 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С 24 фа мажор сделать по образцу до мажора на странице 23.\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 12, письменно ответить на выопросы стр. 90\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> 1) Учебник баева зебряк номер 169, разобрать ноты (чтобы быстро их узнавать, а не думать про каждую ноту по 2 минуты)\n 2) научиться дирижировать на 4/4\n\n"
                      "<b><i>Слушание музыки:</i></b> Выучить ответы на вопросы урока 'Воспоминание', в разных редакциях уроки 15 или 16 \n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник: номера 169-171 разобрать\n\n"
                      "<b><i>Слушание музыки:</i></b> Уроки 12-13, письменно ответить на вопросы стр. 88\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Сделать классную работу (построить TSD53 с обращениями в тональности фа мажор)\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 12 письменно ответить на вопросы стр. 90\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник: номера 169-171 разобрать"
                      "\n\n<b><i>Музыкальная литература:</i></b> Уроки 12-13 письменно ответить на вопросы стр. 88\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Классную работу (D7 с обращениями и разрешениями сделать в фа мажоре"
                      "\n\n<b><i>Музыкальная литература:</i></b> стр. 258-265\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> В тетради в Des-dur  составить цепочку аккордов и петь\nЦепочка: Т6, Т53, S64, D6, D64, T6, S6, S6(г), D 53"
                      "\n\n<b><i>Музыкальная литература:</i></b> Прочитать в учебнике биографию римского-корсакова и составить таблицу. Три колонки. Первая - дата. Вторая - событие в жизни композитора 3 - произведение, которое он писал в этот период. (третья колонка не всегда может быть заполнена, иногда есть только дата и событие из жизни)\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\nРт. С 24 фа мажор сделать по образцу до мажора на странице 23.", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\nВ тренажёре слушать интервалы", parse_mode='HTML')

    elif(message.text == "24 января 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Р.Т. с.25 №9 F-dur\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 13, письменно ответить на вопросы стр. 94\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Р.Т. с.14 №20 'а', 'б', 'в' - только определить вид минора\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 11 или 12 'О превращениях'\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задание прежнее\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 14, письменно ответить на вопросы стр. 99 (1-4)\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник: №106 разобрать (по нему будет диктант)\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 13, письменно ответить на вопросы стр. 94\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Задание прежнее"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 14, письменно ответить на вопросы стр. 99 (1-4)\n\n"
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник: №106 разобрать (по нему будет диктант)"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 30, письменно ответить на вопросы стр. 268\n\n"
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Р.Т. с.26 №22 'А'"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 28 читать, ответить на вопросы и слушать сюиту\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')
     
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\n Р.Т. с.25 №9 F-dur\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\n Р.Т. с.31 №16'A', 17\n", parse_mode='HTML')

    elif(message.text == "31 января 2026"):
     bot.send_message(message.chat.id,                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Группа в 11:40:В учебнике номер 211 петь с дирижированием\n\nГруппа в 12:20: В учебнике номер 211 прохлопать ритм со счётом (на раз и два и три и четыре и)\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 13, письменно ответить на вопросы стр 94\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> В учебнике номер 184 разобрать как в классе (определить тональность, прохлопать ритм, разобрать ноты). И проговорить ноты с дирижированием (не петь).\n\n"
                      "<b><i>Слушание музыки:</i></b> Уроки 11,12, выучить слова из урока 15\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Написать диктант, используя подсказки в тетради. Подписать все аккорды, которые встречаются в диктанте. Сам диктант далее в сообщениях.\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 14, письменно ответить на вопросы стр 99(1-4)\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Написать диктант, используя подсказки в тетради (на уроке мы разобрали ритм, который может встретится, и построили аккордовую цепочку, которая звучит в диктанте). Сам диктант далее в сообщениях.\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 13, письменно ответить на вопросы стр 94\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио: Написать диктант, используя подсказки в тетради. Подписать все аккорды, которые встречаются в диктанте. Сам диктант далее в сообщениях.</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 14, письменно ответить на вопросы стр 99(1-4)\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Написать диктант, используя подсказки в тетради (на уроке мы разобрали ритм, который может встретится, и построили аккордовую цепочку, которая звучит в диктанте). Сам диктант далее в сообщениях."
                      "\n\n<b><i>Музыкальная литература:</i></b> урок 30, письменно ответить на вопросы стр 268\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> https://xn--80ahdkilbo1bvw1el.xn--p1ai/test/?mode=7 \nВ тренажёре слушать:\n1) обращения D7с разрешением\n2) Трезвучия (Б,М, Ув, Ум)"
                      "\n\n<b><i>Музыкальная литература:</i></b> Перечитать уроки 29 и 30\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n Класса нет",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "Диктант 4 и 6 классы: https://disk.yandex.ru/d/iGXscLdo8WX6aw", parse_mode='HTML')
     bot.send_message(message.chat.id, "Диктант 5 класс: https://disk.yandex.ru/d/axc2WJjnjW1e2A", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b> Группа в 11:40:В учебнике номер 211 петь с дирижированием\n\nГруппа в 12:20: В учебнике номер 211 прохлопать ритм со счётом (на раз и два и три и четыре и)\n", parse_mode='HTML')
     bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/PvMDM9FlPC_4LQ', caption="<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b> 1) рт. С. 31 номер 18\n2) подписать интервалы\n", parse_mode='HTML')

    elif(message.text == "7 февраля 2026"):     
     bot.send_message(message.chat.id,                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 14 номер 16\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 14, письменно ответить на вопросы стр 101\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> 1) рт. С. 23 номер 4\n2) в учебнике номера 178,179 петь с дирижированием и со словами\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 13\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> В учебнике номера 393, 394 петь с дирижированием\n\n"
                      "<b><i>Слушание музыки:</i></b> Урок 15, письменно ответить на вопросы стр 108\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 11 номер 1 (е) построить и петь\n\n"
                      "<b><i>Музыкальная литература:</i></b> Урок 14, письменно ответить на вопросы стр 101\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> В учебнике номера 393, 394 петь с дирижированием"
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 15, письменно ответить на вопросы стр 108\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 13 номер 10 (вторая строчка)\nС. 25 номер 2 до минор. Построить и петь."
                      "\n\n<b><i>Музыкальная литература:</i></b> Урок 31 стр 270-273, письменно ответить на вопросы стр 275(1-3)\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> В учебнике номера 396, 400 петь с дирижированием"
                      "\n\n<b><i>Музыкальная литература:</i></b> Сделать конспект по презентации (она есть у них в чате в телеграмме)\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Класса нет"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b> Рт. С. 14 номер 16\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b> Рт. С. 14 номера 16,17\n", parse_mode='HTML')

    elif(message.text == "14 февраля 2026"):
     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Группа в 11:40: Рт. С. 29 номера 1,2,3\nГруппа в 12:20 Рт. С. 16 номер 24 (б, в),Номер 25 (а)\n\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Рт. С. 23 номера 5,6,7\n\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b> 1) учебник номера 393, 394 петь с дирижированием\n2) рт. С. 27 номер 1\n\n"
                      "<b><i>Слушание музыки:</i></b> Задания нет\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник номер 404 поохлопать ритм со счётом как в классе\nНомер 405 разобрать самостоятельно\n\n"
                      "<b><i>Музыкальная литература:</i></b> Задания нет\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник номера 393, 394 петь с дирижированием"
                      "\n\n<b><i>Музыкальная литература:</i></b> Задания нет\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b> Учебник номер 404 прохлопать ритм со счётом как в классе\nНомер 405 разобрать самостоятельно"
                      "\n\n<b><i>Музыкальная литература:</i></b> Задания нет\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b> рт. С. 26 номер 21 в, г"
                      "\n\n<b><i>Музыкальная литература:</i></b> конспект по презентации\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио: Класса нет</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b> Класса нет\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>Группа в 11:40: Рт. С. 29 номера 1,2,3\nГруппа в 12:20 Рт. С. 16 номер 24 (б, в),Номер 25 (а)\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b> Построить в нотной тетради мажорные трезвучия от всех белых клавиш\n", parse_mode='HTML')

    elif(message.text == "21, 23 февраля 2026(locked)"):     
     bot.send_message(message.chat.id,                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\n", parse_mode='HTML')

    elif(message.text == "28 февраля, 2 марта 2026(locked)"):     
     bot.send_message(message.chat.id,                      
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\n", parse_mode='HTML')

    elif(message.text == "7, 9 марта 2026"):     
     bot.send_message(message.chat.id,           
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\n", parse_mode='HTML')

    elif(message.text == "14, 16 марта 2026"):     
     bot.send_message(message.chat.id,
                      "<b><i>1 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>2 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n "
                      
                      "<b><i>3 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Слушание музыки:</i></b>\n\n " 
                      
                      "<b><i>4 класс:</i></b>\n<b><i>Сольфеджио:</i></b>\n\n"
                      "<b><i>Музыкальная литература:</i></b>\n\n"
                      
                      "<b><i>5 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>6 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>7 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n\n "
                      
                      "<b><i>8 класс:</i></b>\n<b><i>Сольфеджио:</i></b>"
                      "\n\n<b><i>Музыкальная литература:</i></b>\n",
                         parse_mode='HTML')

     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (7-9 лет):</i></b>\n", parse_mode='HTML')
     bot.send_message(message.chat.id, "<b><i>1 кл. внебюджет, сольфеджио (10-14 лет):</i></b>\n", parse_mode='HTML')

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
