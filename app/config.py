from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    database_url: str
    jwt_secret: str
    jwt_alg: str = "HS256"
    access_token_minutes: int = 120
    cors_origins: str = "http://localhost:5173"
    demo_user_email: str | None = None
    demo_user_password: str | None = None

    class Config:
        env_prefix = ""
        case_sensitive = False

    def cors_list(self):
        return [s.strip() for s in self.cors_origins.split(",") if s.strip()]


settings = Settings()
