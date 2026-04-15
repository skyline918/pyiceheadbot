from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


router = APIRouter()


@router.post('/api/v1/users/login')
def login_endpoint(request: Request) -> Response:
    return JSONResponse(status_code=200, content={'pon': 'daun'})


@router.post('/api/v1/users/login')
def register(request: Request) -> Response:
    return JSONResponse(status_code=200, content={'pon': 'daun'})
