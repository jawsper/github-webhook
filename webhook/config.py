import shlex

from pydantic import BaseSettings

class Config(BaseSettings):
    github_secret: str
    match_tag: str = "latest"
    command: list[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str):
            if field_name == "command":
                return shlex.split(raw_val)
            return raw_val


config = Config()  # type: ignore
