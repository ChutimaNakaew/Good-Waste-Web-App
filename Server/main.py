import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# app = FastAPI()
# templates = Jinja2Templates(directory="../Web")

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

# @app.get("/test")
# async def test(request: Request):
# 	return employee.html

# @app.get("/")
# async def home(request: Request):
# 	return templates.TemplateResponse("index.html",{"request":request})


# @app.get("/reward")
# async def home(request: Request):
# 	return templates.TemplateResponse("reward.html",{"request":request})
