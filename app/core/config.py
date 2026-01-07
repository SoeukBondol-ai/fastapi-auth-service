from pydantic_settings import BaseSettings, SettingsConfigDict# Pydantic new version are different from old

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    JWT_SECRET : str 
    JWT_ALGORITHM: str = "HS256"

    model_config= SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
