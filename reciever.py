import time
from datetime import datetime
import requests

after = 0

def get_messages():
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    data = response.json()
    return data['messages']

# Print Message with customised time
def print_message(message):
    username = message['username']
    message_time = message['time']
    text = message['text']

    dt = datetime.fromtimestamp(message_time)

    print(dt.strftime('%d.%m.%Y %H:%M:%S'), username)
    print(text)
    print()


while True:
    messages = get_messages()

    for message in messages:
        print_message(message)
        if message['time'] > after:
            after = message['time']

    time.sleep(5)