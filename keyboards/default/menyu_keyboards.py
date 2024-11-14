from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar🛍"),
        ],
        [
            KeyboardButton(text="🤝 Yordam"),
        ],
    ],resize_keyboard=True
)

location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
location_keyboard.add(KeyboardButton("Lokatsiyani yuborish 📍", request_location=True))