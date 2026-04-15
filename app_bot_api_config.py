from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    postgresql_conn: str

