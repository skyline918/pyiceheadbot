from contextlib import asynccontextmanager

import uvicorn
from asyncpg import create_pool
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.users_and_auth import router as auth_router
from api.discord import router as discord_router
from app_bot_api_config import BotSettings
from app_bot_api_state import BotApiState
from infrastructure.log import get_logger
from service.init_tables import create_all_tables


logger = get_logger(__name__)


def main():
    settings = BotSettings()
    state = BotApiState()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        state.pool = await create_pool(dsn=settings.postgresql_conn, min_size=2, max_size=2)
        logger.info("Postgresql connection pool is created")

        app.state.pool = state.pool

        await create_all_tables(state)
        yield

        await state.pool.close()
        logger.info("Postgresql connection pool is closed")

    fast_api = FastAPI(lifespan=lifespan)

    fast_api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fast_api.include_router(auth_router)
    fast_api.include_router(discord_router)

    uvicorn.run(fast_api, host="0.0.0.0", port=8888)



if __name__ == '__main__':
    main()