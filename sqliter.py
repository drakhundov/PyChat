import sqlite3
import hashlib


class DataBase:
    def __init__(self, name='database.db'):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.commit()
        self.close()

    def add_user(self, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        self.cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))

    def check_user(self, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return True if self.cursor.fetchall() else False
    
    def user_exists(self, username):
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return True if self.cursor.fetchall() else False

    def add_message(self, message):
        self.cursor.execute('INSERT INTO messages VALUES (?, ?, ?, ?)', tuple(message.values()))

    def get_last_user_messages(self, username, after):
        self.cursor.execute('SELECT username, text, time FROM messages WHERE receiver = ? AND time > ?', (username, after))
        return self.cursor.fetchall()
    
    def delete_all_messages(self):
        self.cursor.execute('DELETE FROM messages')

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()