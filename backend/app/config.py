"""Configuration settings using Pydantic BaseSettings."""

from pydantic import BaseSettings, PostgresDsn, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "Energy Consulting Platform"
    PROJECT_DESCRIPTION: str = "Platform for energy usage analysis and consulting"
    PROJECT_VERSION: str = "0.1.0"

    DATABASE_URL: PostgresDsn
    REDIS_URL: str = Field(default="redis://localhost:6379")
    RABBITMQ_URL: str = Field(default="amqp://guest:guest@localhost:5672/")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
