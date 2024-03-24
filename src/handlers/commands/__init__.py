__all__ = ("router",)

from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .user_commands import router as user_commands_router

router = Router(name=__name__)

router.include_routers(
    start_router,
    help_router,
    user_commands_router,
)
