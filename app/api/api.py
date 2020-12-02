from fastapi import APIRouter

from app.api.process import process


api_router = APIRouter()

# api_router.include_router(root.router)
api_router.include_router(process.router, prefix="/process", tags=["Process"])
