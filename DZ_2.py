import requests
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
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()
    numbers_of_astronauts = astronauts.get('number')
    return str(numbers_of_astronauts)


if __name__ == '__main__':
    app.run()
