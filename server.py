# By using Flask and Python we create server.
from flask import Flask, request
import datetime as dt
import time

app = Flask(__name__)

messages = []

users = {
    'Dimitrij': 'Dimitrij12345'
}

@app.route("/")
def hello():
    return "This is Dimitrij Chat App using Flask and Python. dimitrij@aleshkov.com"

# create Json page with information about Messanger name, actual datetime, amout of messages and users.
@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Py messenger',
        'time': dt.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
        'users': len(users),
        'messages': len(messages),
    }

@app.route("/send", methods=['POST'])
def send():
    username = request.json['username']
    password = request.json['password']

    if username in users:
        if password != users[username]:
            abort(401)
    else:
        users[username] = password

    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)
    return {'ok': True}

@app.route("/messages")
def messages_view():
    after = float(request.args.get('after'))
    filtered_messages = [message for message in messages if message['time'] > after]

    #for message in messages:
    #    if message['time'] > after:
    #        filtered_messages.append(message)

    return{
        'messages': filtered_messages
    }

app.run()

