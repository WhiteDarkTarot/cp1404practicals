from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

    return '<h1>Hello World :)</h1>'


@app.route('/greet')
def greet():
    return "Hello"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Siyi_Liu"):
    return f"Hello {name}"


if __name__ == '__main__':
    app.run()
