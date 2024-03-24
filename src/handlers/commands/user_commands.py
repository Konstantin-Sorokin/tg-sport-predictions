from aiogram import Router, types, F

from src.keyboards.user_keyboards import StartButton

router = Router(name=__name__)


@router.message(F.text == StartButton.PROFILE)
async def handle_profile_command(message: types.Message):
    await message.answer(
        text="Это профиль",
    )


@router.message(F.text == StartButton.PREDICTIONS)
async def handle_predictions_command(message: types.Message):
    await message.answer(
        text="Это прогнозы",
    )


@router.message(F.text == StartButton.SEASONS)
async def handle_seasons_command(message: types.Message):
    await message.answer(
        text="Это сезоны",
    )
