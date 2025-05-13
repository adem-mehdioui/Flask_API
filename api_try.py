# filepath: d:\Ecole HETIC\MD5\data-apps\Dev\Flask_API\api_try.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')



@app.route('/name', methods=['GET', 'POST'])
def myname():
   return "Adem MEHDIOUI."

@app.route('/promotion_name', methods=['GET', 'POST'])
def promotion_name():
   return "Promotion MD5 204/2025"


# calculator
@app.route('/add/<int:a>/<int:b>', methods=['GET', 'POST'])
def calculator(a, b):
    return str(a + b)

@app.route('/subtract/<int:a>/<int:b>', methods=['GET', 'POST'])
def subtract(a, b):
    return str(a - b)

@app.route('/multiply/<int:a>/<int:b>', methods=['GET', 'POST'])
def multiply(a, b):
    return str(a * b)

@app.route('/divide/<int:a>/<int:b>', methods=['GET', 'POST'])
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return str(a / b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)