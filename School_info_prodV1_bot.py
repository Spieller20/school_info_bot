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
    btn3 = types.KeyboardButton("Кордон")
    markup.add(btn1, btn2, btn3)
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
     btn1 = types.KeyboardButton("6 сентября 2025")
     btn2 = types.KeyboardButton("13 сентября 2025")
     btn3 = types.KeyboardButton("20 сентября 2025")
     btn4 = types.KeyboardButton("27 сентября 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Октябрь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("4 октября 2025")
     btn2 = types.KeyboardButton("11 октября 2025")
     btn3 = types.KeyboardButton("18 октября 2025")
     btn4 = types.KeyboardButton("25 октября 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Ноябрь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("1 ноября 2025")
     btn2 = types.KeyboardButton("8 ноября 2025")
     btn3 = types.KeyboardButton("15 ноября 2025")
     btn4 = types.KeyboardButton("22 ноября 2025")
     btn5 = types.KeyboardButton("29 ноября 2025")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Декабрь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("6 декабря 2025")
     btn2 = types.KeyboardButton("13 декабря 2025")
     btn3 = types.KeyboardButton("20 декабря 2025")
     btn4 = types.KeyboardButton("27 декабря 2025")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Январь"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("3 января 2026")
     btn2 = types.KeyboardButton("10 января 2026")
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
     btn3 = types.KeyboardButton("21 февраля 2026")
     btn4 = types.KeyboardButton("28 февраля 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Март"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("7 марта 2026")
     btn2 = types.KeyboardButton("14 марта 2026")
     btn3 = types.KeyboardButton("21 марта 2026")
     btn4 = types.KeyboardButton("28 марта 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Апрель"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("4 апреля 2026")
     btn2 = types.KeyboardButton("11 апреля 2026")
     btn3 = types.KeyboardButton("18 апреля 2026")
     btn4 = types.KeyboardButton("25 апреля 2026")
     btn5 = types.KeyboardButton("Домашние задания")
     btn6 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)

    elif(message.text == "Май"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("2 мая 2026")
     btn2 = types.KeyboardButton("9 мая 2026")
     btn3 = types.KeyboardButton("16 мая 2026")
     btn4 = types.KeyboardButton("23 мая 2026")
     btn5 = types.KeyboardButton("30 мая 2026")
     btn6 = types.KeyboardButton("Домашние задания")
     btn7 = types.KeyboardButton("Главное меню")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
     bot.send_message(message.chat.id,text="Выберите дату урока", reply_markup=markup)  

    
    #Меню выбранной даты урока
    elif(message.text == "6 сентября 2025"):     
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

    elif(message.text == "13 сентября 2025"):     
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
     
    elif(message.text == "20 сентября 2025"):     
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

    elif(message.text == "27 сентября 2025"):     
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

    elif(message.text == "4 октября 2025"):     
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

    elif(message.text == "11 октября 2025"):     
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

    elif(message.text == "18 октября 2025"):     
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

    elif(message.text == "25 октября 2025"):     
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

    elif(message.text == "1 ноября 2025"):     
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

    elif(message.text == "8 ноября 2025"):     
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

    elif(message.text == "15 ноября 2025"):     
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

    elif(message.text == "22 ноября 2025"):     
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

    elif(message.text == "29 ноября 2025"):     
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

    elif(message.text == "6 декабря 2025"):     
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

    elif(message.text == "13 декабря 2025"):     
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

    elif(message.text == "20 декабря 2025"):     
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

    elif(message.text == "27 декабря 2025"):     
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

    elif(message.text == "3 января 2026"):     
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

    elif(message.text == "10 января 2026"):     
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

    elif(message.text == "17 января 2026"):     
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

    elif(message.text == "24 января 2026"):     
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

    elif(message.text == "31 января 2026"):     
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

    elif(message.text == "7 февраля 2026"):     
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

    elif(message.text == "14 февраля 2026"):
     
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

    elif(message.text == "21 февраля 2026"):     
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

    elif(message.text == "28 февраля 2026"):     
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

    elif(message.text == "7 марта 2026"):     
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

    elif(message.text == "14 марта 2026"):     
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

    elif(message.text == "21 марта 2026"):     
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

    elif(message.text == "28 марта 2026"):     
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

    elif(message.text == "4 апреля 2026"):     
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

    elif(message.text == "11 апреля 2026"):     
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

    elif(message.text == "18 апреля 2026"):     
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

    elif(message.text == "25 апреля 2026"):     
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

    elif(message.text == "2 мая 2026"):     
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

    elif(message.text == "9 мая 2026"):     
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

    elif(message.text == "16 мая 2026"):     
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

    elif(message.text == "23 мая 2026"):     
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
     btn3 = types.KeyboardButton("Кордон")   
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id, text="О чём Вы хотите узнать?", reply_markup=markup)
    else:
     bot.send_message(message.chat.id, text="Информация по запросу пока недоступна или запрос не соответствует логике сервиса.")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
