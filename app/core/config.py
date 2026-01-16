from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Employee Management API"

    # JWT settings
    SECRET_KEY: str = "SECRET123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database
    DATABASE_URL: str = "sqlite:///./employees.db"

    class Config:
        env_file = ".env"


settings = Settings()
