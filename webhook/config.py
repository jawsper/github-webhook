from pydantic import BaseSettings


class Config(BaseSettings):
    github_secret: str
    match_tag: str = "latest"
    command: str


config = Config()  # type: ignore
