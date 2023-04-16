import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/rewards')
def home():
   return render_template('reward.html')
if __name__ == '__main__':
   app.run()
  
