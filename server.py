import sys, time

from flask import Flask, request

from sqliter import DataBase


app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send_message():
    msg = {
        'username': request.args['username'],
        'receiver': request.args['receiver'],
        'text': request.args['text'],
        'time': time.time()
    }

    with DataBase() as db:
        db.add_message(msg)

    return {'ok': True}


@app.route('/get')
def get_messages():
    username = request.args['username']
    after = float(request.args['after'])

    with DataBase() as db:
        if last_messages := db.get_last_user_messages(username, after):
            return {'messages': [{'username': message[0],
                                  'text': message[1],
                                  'time': message[2]}
                                for message in last_messages]}

        else:
            return {'messages': []}


@app.route('/users/<string:name>')
def user(name):
    password = request.args['password']

    with DataBase() as db:
        check = db.check_user(name, password)
        exists = db.user_exists(name)

    return {'exists': exists, 'check': check}


@app.route('/users/new', methods=['POST'])
def new_user():
    username = request.args['username']
    password = request.args['password']

    with DataBase() as db:
        db.add_user(username, password)


if __name__ == '__main__':
    debug = ('--debug' in sys.argv)
    app.run(debug=debug)