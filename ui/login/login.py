import requests

import pyform
import config

class LogIn(pyform.Form):
    def start(self):
        self.username = pyform.widgets.Input(self.form)
        self.username.place(36, 25)

        self.password = pyform.widgets.Input(self.form, show='*')
        self.password.place(36, 60)

        self.submit = pyform.widgets.Button(self.form, 'submit')
        self.submit.place(65, 100)
        self.submit.set_size(10, 1)
        self.submit.on_click(self.login)

    def login(self):
        info = {
            'username': self.username.text(), 
            'password': self.password.text()
        }

        response = requests.get(
            '{server}/users/{username}'.format(
                server=config.SERVER,
                username=info['username']),
            params={'password': info['password']}).json()

        if not response['check']:
            pyform.message('Invalid Credentials')

            if not response['exists'] and pyform.ask('Do You Want To Register?'):
                requests.post('{server}/users/new'
                              .format(server=config.SERVER),
                              params=info)
            else:
                pass
        else:
            self.info = info # pass credentials to main program

            pyform.run('main')
            pyform.quit('login')

    def keydown(self, key):
        if key == 'enter':
            self.login()