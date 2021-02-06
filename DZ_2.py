from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return 'Choice options: /requirements/, /generate-users/, /mean/, /space/'


@app.route('/requirements/')
def returning_content():
    file = open('requirements.txt', 'r')
    data = file.read()
    return data


@app.route('/generate-users/')
def user_generation():
    return 'Hello, World!'


@app.route('/mean/')
def average_indicators():
    return 'Hello, World!'


@app.route('/space/')
def number_of_astronauts():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
