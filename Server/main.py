from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
# templates = Jinja2Templates(directory="Server")

from pathlib import Path
BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "template"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("employee.html",{"request":request})


@app.get("/reward", response_class=HTMLResponse)
async def home(request: Request):
	return templates.TemplateResponse("reward.html",{"request":request})
