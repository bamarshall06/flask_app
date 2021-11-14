from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>DIY Money</h1>'


@app.route('/<name>')
def firstname(name):
    return f'<h1>Hello DIYer Money Man - {name}. You can be great with your money all on your own.</h1>'


if __name__ == '__main__':
    app.run(debug=True)
