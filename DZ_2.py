import requests
import pandas as pd
from flask import Flask
from faker import Faker
import string
import random

app = Flask(__name__)


def generate_str():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(8))
    return random_string


@app.route('/')
def start():
    return 'Choice options: /requirements/, /generate-users/, /mean/, /space/'


@app.route('/requirements/')
def returning_content():
    with open('requirements.txt', 'r') as file:
        data = file.read()
    return data


@app.route('/generate-users/')
def generate_users():
    fake_names = []
    fake = Faker()
    for _ in range(100):
        fake_names.append(fake.name())
    users_list = [f'{"_".join(name.split(" "))} {generate_str()}@gmail.com' for name in fake_names]
    users = ';'.join(users_list)
    return users


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
