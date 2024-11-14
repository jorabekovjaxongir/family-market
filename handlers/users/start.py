from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startKeyboard import phone_keyboard
from keyboards.default.menyu_keyboards import main_menu

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum xurmatli <b>{message.from_user.full_name}\nFamiliy market</b> botiga xush kelibsiz!\n\n<b>\"Mahsulotlar🛍\"</b> tugmasini bosing",reply_markup=main_menu)


