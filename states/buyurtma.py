from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderState(StatesGroup):
    name = State()
    phone = State()
    location = State()
    waiting_for_card =State()
