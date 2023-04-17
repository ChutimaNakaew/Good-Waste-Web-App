from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="Web")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})


@app.get("/reward", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("reward.html",{"request":request})
