from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class StartButton:
    PROFILE = "Профиль"
    PREDICTIONS = "Прогнозы"
    SEASONS = "Сезоны"


def get_start_kb():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=StartButton.PREDICTIONS),
                KeyboardButton(text=StartButton.SEASONS),
            ],
            [
                KeyboardButton(text=StartButton.PROFILE),
            ],
        ],
    )
