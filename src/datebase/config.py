from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017/"
    MONGO_INITDB_DATABASE: str = "AddressBook"
    REDIS_DOMAIN: str = "localhost"
    REDIS_PORT: int = 6379

    class Config:
        extra = "ignore"
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
