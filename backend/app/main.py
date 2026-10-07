from fastapi import FastAPI

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