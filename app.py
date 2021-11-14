from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Moto</h1>'


@app.route('/<name>')
def firstname(name):
    return f'<h1>Hello Moto {name} the big sec </h1>'


if __name__ == '__main__':
    app.run(debug=True)
