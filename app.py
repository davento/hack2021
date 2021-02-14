from flask import Flask, request, jsonify, render_template, Response
import psycopg2
import json

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/register', methods = ['POST'])
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
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'User cannot not be created'})
            return Response(msg, status=400)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'User created'})
            return Response(msg, status=201)


@app.route('/publish', methods = ['POST'])
def publish():
    title = request.args.get('content')
    publisher = request.args.get('publisher')
    date = request.args.get('date') 
    link = request.args.get('link') 
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        query = """INSERT INTO paper VALUES (%s, %s, %s, %s);"""
        values = (title, publisher, date, link)
        cursor.execute(query, values)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'Paper reference cannot not be created'})
            return Response(msg, status=400)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'Paper reference created'})
            return Response(msg, status=201)

@app.route('/get10Paper', methods = ['GET'])
def paper():
    msg = []
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        query = "SELECT * FROM papers"
        cursor.execute(query)
        record = cursor.fetchall()
        for row in record:
            obj = {}
            obj['title'] = row[0]
            obj['publisher'] = row[1]
            obj['publicationDate'] = row[2]
            obj['link'] = row[3]
            msg.append(obj)
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'Cannot get papers'})
            return Response(msg, status=400)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            resp = json.dumps(msg)
            return Response(resp, status=200)


@app.route('/createDiscussion', methods = ['POST'])
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
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'Discussion cannot not be created'})
            return Response(msg, status=400)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'Discussion created'})
            return Response(msg, status=201)


@app.route('/createSubdiscussion', methods = ['POST'])
def createSubdiscussion():
    fid = request.args.get('fid')
    content = request.args.get('content')
    username = request.args.get('username') 
    paperTitle = request.args.get('paperTitle') 
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="ergo")
        cursor = connection.cursor()
        query = """INSERT INTO dpoint VALUES (DEFAULT, %s, %s, DEFAULT, DEFAULT, %s, %s);"""
        values = (fid, content, username, paperTitle)
        cursor.execute(query, values)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        if (connection):
            msg = json.dumps({'message': 'subdiscussion cannot not be created'})
            return Response(msg, status=400)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            msg = json.dumps({'message': 'Subdiscussion created'})
            return Response(msg, status=201)


if __name__ == '__main__':
    app.run()
