import redis
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int = 5, window: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window = window

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        key = f"rate_limit:{client_ip}"

        current = redis_client.incr(key)
        if current == 1:
            redis_client.expire(key, self.window)

        if current > self.limit:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests. Please slow down."},
            )

        return await call_next(request)
