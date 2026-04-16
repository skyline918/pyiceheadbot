from app_bot_api_state import BotApiState


async def create_all_tables(state: BotApiState):
    async with state.pool.acquire(timeout=10) as conn:
        await conn.execute('''
        CREATE TABLE IF NOT EXISTS discord_servers (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            img_url VARCHAR(255)
        )
        ''')
