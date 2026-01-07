from fastapi import FastAPI
from app.api.v1.router import api_router
from app.middlewares.rate_limit import RateLimitMiddleware

app = FastAPI(title="FastAPI Clean Architecture")


app.add_middleware(RateLimitMiddleware)

app.include_router(api_router, prefix="/api/v1")
