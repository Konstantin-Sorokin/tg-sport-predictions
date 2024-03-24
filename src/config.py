from functools import lru_cache
from dotenv import find_dotenv
from pydantic import BaseModel, SecretStr
from pydantic_settings import (
    BaseSettings as _BaseSettings,
    SettingsConfigDict,
)


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8",
    )


class Telegram(BaseSettings, env_prefix="TELEGRAM_"):
    token: SecretStr


class Settings(BaseModel):
    telegram: Telegram


@lru_cache(maxsize=1)
def get_settings():
    return Settings(
        telegram=Telegram(),
    )
