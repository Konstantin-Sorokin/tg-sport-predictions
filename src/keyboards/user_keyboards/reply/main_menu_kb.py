from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Button:
    PROFILE = "Профиль"
    PREDICTIONS = "Прогнозы"
    SEASONS = "Сезоны"


def get_main_menu_kb():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=Button.PREDICTIONS),
                KeyboardButton(text=Button.SEASONS),
            ],
            [
                KeyboardButton(text=Button.PROFILE),
            ],
        ],
    )
