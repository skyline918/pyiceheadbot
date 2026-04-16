from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.get('/api/v1/discord/servers')
async def endpoint_discord_servers(request: Request) -> Response:
    return JSONResponse(status_code=200, content={'pon': 'daun'})