from fastapi import FastAPI
from src.routers.currency_router import router

app = FastAPI(
    title='Currency Change'
)

app.include_router(router)
