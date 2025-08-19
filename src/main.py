from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.currency_router import router

app = FastAPI(
    title='Currency Change'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
