from fastapi import FastAPI
from app.api.v1.router import router

app = FastAPI(
    title="AI Engine",
    version="1.0.0"
)

app.include_router(router)