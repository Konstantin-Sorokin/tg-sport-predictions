from aiogram import Router, types
from aiogram.filters import CommandStart

from src.keyboards.user_keyboards.reply.main_menu_kb import get_main_menu_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start_command(message: types.Message):
    await message.answer(
        text="Hello",
        reply_markup=get_main_menu_kb(),
    )
