from flask import Flask, request
import sqlite3
import random

app = Flask(__name__)


@app.route('/users/list/')
def users_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/create/')
def users_create():

    first_name = request.args['firstName']
    last_name = request.args['lastName']
    is_student = int(request.args['isStudent'] == 'true')
    ID = random.randint(1, 100_000)

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO users VALUES ({ID}, '{first_name}', '{last_name}', {is_student});"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/phones/create/')
def phones_create():

    phone = request.args['phone']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO phones VALUES (null, '{phone}', '{user_id}');"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/phones/list/')
def phones_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM phones;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/phones/')
def users_phones():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.id, users.first_name, users.last_name, phones.value
        FROM users
        INNER JOIN phones ON phones.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/emails/list/')
def emails_list():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM emails;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/emails/create/')
def emails_create():

    email = request.args['email']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO emails VALUES (null, '{email}', '{user_id}');"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/emails/update/')
def emails_update():
    email = request.args['email']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"UPDATE emails SET value = '{email}' WHERE emails.user_id = '{user_id}';"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/emails/delete/')
def emails_delete():
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"DELETE FROM emails WHERE emails.user_id = '{user_id}';"
        cursor.execute(query)

        connection.commit()
    finally:
        connection.close()

    return 'OK'


@app.route('/users/emails/')
def users_emails():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT users.first_name, users.last_name, users.id, emails.value
        FROM users
        INNER JOIN emails ON emails.user_id = users.id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
