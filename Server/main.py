from typing import Union
from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from os.path import dirname, join
import os

app = FastAPI()
templates = Jinja2Templates(directory="../Web")

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})


@app.get("/test")
async def home(request: Request):
	return templates.TemplateResponse("reward.html",{"request":request})
