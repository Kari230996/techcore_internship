from dotenv import load_dotenv
import os
from fastapi import HTTPException, Header
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


async def verify_token(authorization: str = Header(default=None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization Header"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid token format"
        )

    token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token or expired token"
        )


def require_role(role: str):
    async def dependency(authorization: str = Header(default=None)):
        payload = await verify_token(authorization)

        user_role = payload.get("role")
        if user_role != role:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Required role: {role}"
            )

        return payload

    return dependency
