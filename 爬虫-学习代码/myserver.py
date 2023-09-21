from flask import Flask,render_template
from flask import make_response
import json
app = Flask(__name__)

@app.route('/')
def index():
          return render_template('login.html')

@app.route('/data')
def data():
          data = [
                    {'id':1,'name':'学习 good study'},
                    {'id':2,'name':'学习 day up'},
                    {'id':3,'name':'学习 studay！'},
                    ]
          response = make_response(json.dumps(data))
          return response

if __name__ == '__main__':
          app.run(host='0.0.0.0',port='1234')
