import requests
import time


class User:
    def __init__(self, name, server):
        self.name = name
        self.last = time.time() - 24 * 60 * 60
        self.server = server

    def send_message(self, message_text, receiver):
        message = {'username': self.name,
                   'receiver': receiver,
                   'text': message_text}
        
        requests.post(self.server.sender, params=message)

    def get_messages(self):
        info = {
            'username': self.name,
            'after': self.last
        }
        
        response = requests.get(self.server.receiver, params=info).json()

        messages = response['messages']

        if messages:
            self.last = max([float(message['time']) for message in messages])
            return messages