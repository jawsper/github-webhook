from pydantic_settings import BaseSettings

class Config(BaseSettings):
    github_secret: str
    match_tag: str = "latest"
    command: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()  # type: ignore
