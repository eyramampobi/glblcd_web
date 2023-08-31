from flask import Flask, render_template


def make_bigger(func):
    def inner():
        big = func()
        return f'<h1>{big}</h1>'
    return inner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whereami')
def whereami():
     return"Ghana!"
    
@app.route('/greet/<name>/<int:age>')
def greet(name,age):
    return f"I am {name} and I'm {age} years old"


if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0')