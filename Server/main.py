import os
from flask import Flask, render_template

app = Flask(__name__,template_folder="")


@app.route('/')
def home():
   
   env_var_colour = os.environ['APP_COLOR']
   
   return render_template("index.html")
    

    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8088")
