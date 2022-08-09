from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    static_path: Path = "frontend/dist/"
    media_path: Path = "../media/"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
