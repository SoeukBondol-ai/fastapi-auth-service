from fastapi import FastAPI
from fastapi.responses import JSONResponse

def register_exception_handlers(app:FastAPI):
    """
        UserService raises ValueError
        ↓
        FastAPI catches it
        ↓
        handler.py converts it
        ↓
        Client gets HTTP 400
    """
    @app.exception_handler(ValueError)
    async def value_error_handler(_, exc: ValueError):
         return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )
        