from app.routers.auth import router as auth_router
from fastapi import FastAPI

from app.routers.users import router as users_router

app = FastAPI(
    title="CloudCampus API",
    description="Smart Campus Management System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "CloudCampus API is running",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(users_router, prefix="/api")
app.include_router(auth_router, prefix="/api")