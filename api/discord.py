from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.get('/api/v1/discord/servers')
async def endpoint_discord_servers(request: Request) -> Response:
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        rows = await conn.fetch(
            '''SELECT * FROM discord_servers''',
        )
        if not rows:
            return JSONResponse(status_code=404, content={"message": "No servers found"})

    return JSONResponse(content=[dict(row) for row in rows])
