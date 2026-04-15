from asyncpg import Pool


class BotApiState:

    def __init__(self):
        self.pool: Pool | None = None
