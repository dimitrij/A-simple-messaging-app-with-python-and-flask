import requests

def send_message(username, password, text):
    message = {'username': username, 'text': text, 'password': password}
    respone = requests.post('http://127.0.0.1:5000/send', json=message)
    return respone.status_code == 200

username = input('Enter your username: ')
password = input('Enter your password: ')

while True:
    text = input()
    result = send_message(username, password, text)
    if result is False:
        print('Error')