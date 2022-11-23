from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn1 = KeyboardButton('Сгенерировать никнейм')
btn2 = KeyboardButton('Сгенерировать пароль')
btn3 = KeyboardButton('Найти аватарку', callback_data="img")

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.row(btn1, btn2)
markup.row(btn3)