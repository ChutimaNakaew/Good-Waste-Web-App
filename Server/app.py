import os
from flask import Flask, render_template

app = Flask(__name__,template_folder="")


@app.route('/home')
def home():
   return render_template("../Web/home.html")
    

@app.route('/rewards')
def rewards():
    return render_template("../Web/reward.html")
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8081")


    
