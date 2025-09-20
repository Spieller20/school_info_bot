<h2>Телеграм бот, который позволяет получить информацию по заранее заданным кнопкам</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Помочь обучающимся и их родителями получить информацию (ДЗ и предметы к учёбе) в любое время суток.

Бот присылает информацию по заранее заданным кнопкам:
* Можно получить информацию о необходимом инвентаре на уроках
* Можно получить информацию о ранее заданных домашних заданиях

## 🖼 Скриншоты

Стартовое меню:

![image](https://raw.githubusercontent.com/Spieller20/school_info_bot/refs/heads/main/Strat.png)

Меню инвентаря:

![image](https://raw.githubusercontent.com/Spieller20/school_info_bot/refs/heads/main/Inventar.png)
![image](https://raw.githubusercontent.com/Spieller20/school_info_bot/refs/heads/main/Predmet.png)

Меню домашних задании:

![image](https://raw.githubusercontent.com/Spieller20/school_info_bot/refs/heads/main/DZ.png)
![image](https://raw.githubusercontent.com/Spieller20/school_info_bot/refs/heads/main/Date.png)

## 💻 Технологии

* Python
* Библиотека `telebot`

## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота
   Примечание: в коде бота нет строчки для токена.

4. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pyTelegramBotAPI
```

``` markdown
python3 -m pip install faker
```

5. Запускаем
``` markdown
python3 card_bot.py
```

## Автор

Иван Белов ([@IvanQA2025](https://t.me/IvanQA2025))
