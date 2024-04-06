from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URL: str
    MONGO_URL: str
    REDIS_DOMAIN: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = None

    class Config:
        extra = "ignore"
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
