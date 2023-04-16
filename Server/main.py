import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import cv2
import base64

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/rewards')
def home():
   return render_template('reward.html')
if __name__ == '__main__':
   app.run()
  
