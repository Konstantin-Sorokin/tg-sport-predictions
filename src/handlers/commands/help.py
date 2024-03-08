from aiogram import Router, types
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command("help"))
async def handle_help_command(message: types.Message):
    await message.answer("Help")
