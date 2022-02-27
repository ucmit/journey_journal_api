from dotenv import load_dotenv
# Загружаем переменные из .env
load_dotenv()

import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routers import journal, user, api
from app.models.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Journey Journal API",
    version="0.0.1a"
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(journal.router)
app.include_router(user.router)
app.include_router(api.router)

app.mount('/static', StaticFiles(directory=os.getenv('STATIC_PATH')), name="static")
templates = Jinja2Templates(directory=os.getenv('TEMPLATES_PATH'))

@app.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)