from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'
    MONGO_URL: str = "mongodb://localhost:27017/"
    MONGO_INITDB_DATABASE: str = "AddressBook"
    REDIS_DOMAIN: str = "localhost"
    REDIS_PORT: int = 6379

    class Config:
        extra = "ignore"
        env_file = "../../.env"
        env_file_encoding = "utf-8"


settings = Settings()
