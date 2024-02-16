from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from .buttons import dog_button, cucumber_button

dog_cucumber_keyboard = ReplyKeyboardMarkup(
    keyboard=[[dog_button, cucumber_button]]
)

remove_keyboard = ReplyKeyboardRemove()
