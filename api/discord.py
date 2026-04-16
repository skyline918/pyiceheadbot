from fastapi import APIRouter, Body
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


@router.post('/api/v1/discord/add-server')
async def endpoint_discord_servers(request: Request) -> Response:
    pool = request.app.state.pool
    data = await request.json()
    name = data.get("name")
    img_url = data.get("img_url")

    if not name:
        return JSONResponse(status_code=404, content={"message": "Not found name"})

    async with pool.acquire() as conn:
        await conn.execute(
            '''INSERT INTO discord_servers (name, img_url) VALUES 
                ($1, $2)
            ''',
            name,
            img_url,
        )

    return JSONResponse(
        status_code=200,
        content={
            "message": "success",
            "data": dict({"name": name, "img_url": img_url})
        }
    )


@router.get('/api/v1/discord/bots')
async def endpoint_discord_bots(request: Request) -> Response:
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        rows = await conn.fetch(
            '''SELECT * FROM discord_bots''',
        )
        if not rows:
            return JSONResponse(status_code=404, content={"message": "No servers found"})

    return JSONResponse(content=[dict(row) for row in rows])
