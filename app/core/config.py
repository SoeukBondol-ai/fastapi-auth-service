from pydantic_settings import BaseSettings  # Pydantic new version are different from old

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    JWT_SECRET : str 
    JWT_ALGORITHM: str = "HS256"

settings = Settings()
