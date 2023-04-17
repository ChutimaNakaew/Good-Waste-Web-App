import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("Web"),
    autoescape=select_autoescape()
)
templates = env.get_template("reward.html")
app = FastAPI()
# templates = Jinja2Templates(directory="../Web")

@app.get("/test")
async def test(request: Request):
	return "Test"

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})

@app.get("/reward")
async def home(request: Request):
	return templates.TemplateResponse("reward.html",{"request":request})
