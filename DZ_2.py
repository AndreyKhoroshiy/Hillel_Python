import requests
import pandas as pd
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
    data = pd.read_csv('hw.csv', index_col='Index')
    data.rename(columns={' "Height(Inches)"': 'Height', ' "Weight(Pounds)"': 'Weight'}, inplace=True)
    average_height_inches = data.Height.mean()
    average_weight_pounds = data.Weight.mean()
    average_height_sm = average_height_inches * 2.54
    average_weight_kg = average_weight_pounds * 0.453592
    return f"Средний рост в см  {average_height_sm}. Средний вес в кг {average_weight_kg}."


@app.route('/space/')
def number_of_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()
    numbers_of_astronauts = astronauts.get('number')
    return str(numbers_of_astronauts)


if __name__ == '__main__':
    app.run()
