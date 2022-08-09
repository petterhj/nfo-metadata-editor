from pathlib import Path

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)

from log import logger
from settings import get_settings, Settings


app = FastAPI()
app.logger = logger


@app.on_event("startup")
async def startup_event():
    logger.info("Starting...")


@app.get("/api/browse")
async def browse(
    path: str = None,
    settings: Settings = Depends(get_settings),
):
    media_path = settings.media_path / path.replace("../", "").strip("/")

    try:
        media_path.resolve(strict=False)
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=f"Path not found: `{media_path}`",
        )

    return []


@app.get(
    "/api/settings",
    response_model=Settings,
)
async def settings(settings: Settings = Depends(get_settings)):
    return settings
