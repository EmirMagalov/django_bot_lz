from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menu=ReplyKeyboardBuilder()
menu.add(
    KeyboardButton(text="Добавить пост"),
    KeyboardButton(text="Посты"),


)
menu.adjust(2)


remove_kb=ReplyKeyboardRemove()