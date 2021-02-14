from flask import Flask, request, jsonify, render_template, Response
import psycopg2
import json

app = Flask(__name__)



@app.route('/register')
def register():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname') 
    username = request.args.get('username') 
    password = request.args.get('password')
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        query = """INSERT INTO my_user VALUES (%s, %s, %s, %s);"""
        values = (firstname, lastname, username, password)
        cursor.execute(query, values)

        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'User cannot not be created'})
            return Response(msg, status=200)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'User created'})
            return Response(msg, status=201)


@app.route('/publish')
def publish():
    title = request.args.get('content')
    publisher = request.args.get('publisher')
    date = request.args.get('date') 
    link = request.args.get('link') 
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        query = """INSERT INTO  VALUES (DEFAULT, %s, %s, DEFAULT, DEFAULT, %s, %s);"""
        values = (str(record[0][0] + 1), content, username, paperTitle)
        cursor.execute(query, values)
        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'Discussion cannot not be created'})
            return Response(msg, status=200)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'Discussion created'})
            return Response(msg, status=201)


@app.route('/createDiscussion')
def createDiscussion():
    content = request.args.get('content')
    username = request.args.get('username') 
    paperTitle = request.args.get('paperTitle') 
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        cursor.execute("SELECT currval(pg_get_serial_sequence('dpoint', 'id'));")
        record = cursor.fetchall()
        query = """INSERT INTO dpoint VALUES (DEFAULT, %s, %s, DEFAULT, DEFAULT, %s, %s);"""
        values = (str(record[0][0] + 1), content, username, paperTitle)
        cursor.execute(query, values)
        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'Discussion cannot not be created'})
            return Response(msg, status=200)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'Discussion created'})
            return Response(msg, status=201)


@app.route('/')
def index():
    return 'We can do it'

if __name__ == '__main__':
    app.run()