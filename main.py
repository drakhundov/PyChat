# pychat v1.0
import sys

import pyform, message, config
from user import User
from ui import LogIn


class Server:
    def __init__(self, url):
        self.url = url
        self.sender = self.url + '/send'
        self.receiver = self.url + '/get'


class Main(pyform.Form):
    def start(self):
        # TODO: create dropdown of friends
        self.receiver_label = pyform.widgets.Text(self.form, 10, 0.5)
        self.receiver_label.place(25, 5)

        self.messages_text = pyform.widgets.Text(self.form, 55, 25, True)
        self.messages_text.place(25, 25)
        self.messages_text.set_text('MESSAGES\n')

        self.message_input = pyform.widgets.Text(self.form)
        self.message_input.place(25, 440)
        self.message_input.set_size(45, 2)

        self.send_message_button = pyform.widgets.Button(self.form, 'Send')
        self.send_message_button.set_size(10, 2)
        self.send_message_button.place(400, 440)
        self.send_message_button.on_click(self.send_message)

        self.user = User(pyform.apps['login'].info['username'], Server(config.SERVER))

    def update(self):
        if messages := self.user.get_messages():
            for msg in messages:
                self.messages_text.add_text('\n' + message.format(msg))
    
    def send_message(self):
        msg = self.message_input.text()
        receiver = self.receiver_label.text()

        self.user.send_message(msg, receiver)

        self.messages_text.add_text('\n' + message.format(
                                             {'username': 'you',
                                              'text': msg}))
        
        self.message_input.reset_text()
    
    def end(self):
        self.form.destroy()
        sys.exit()
        

pyform.add(LogIn, 'login', 'ui\\login\\settings.json')
pyform.add(Main, 'main', 'settings.json')

pyform.run('login')

pyform.mainloop()