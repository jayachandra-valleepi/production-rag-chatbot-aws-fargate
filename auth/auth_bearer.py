from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from auth.jwt_handler import decode_jwt


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):

        token = request.cookies.get("access_token")

        if not token:
            raise HTTPException(status_code=403, detail="Login Required")

        decoded = decode_jwt(token)

        if not decoded:
            raise HTTPException(status_code=403, detail="Invalid Token")

        return token