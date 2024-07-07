"""Config file for project"""

import secrets

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    """Model for database settings"""

    postgres_url: str = Field(validation_alias=AliasChoices("postgres_url", "postgres_dsn", "database_postgres_url"))
    redis_dsn: str = "redis://localhost:6379/15"
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: str
    redis_db: int = 1
    redis_socket_keepalive: bool = True
    title: str = ""
    description: str = ""
    log_level: Literal["debug", "info", "error", "warning", "critical"] = "debug"
    secret: str = secrets.token_hex(32)
    debug: bool = False
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
