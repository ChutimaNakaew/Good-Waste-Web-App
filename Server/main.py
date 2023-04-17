import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from os.path import dirname, join

current_dir = dirname(__file__) 
templates = Jinja2Templates(join(current_dir, 'Web'))

app = FastAPI()

@app.get("/test")
async def test(request: Request):
	return employee.html

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})


@app.get("/reward")
async def home(request: Request):
	return templates.TemplateResponse("reward.html",{"request":request})
