from datetime import datetime
import time


def format(message):
    username = message['username']
    text = message['text']

    if not message.get('time'):
        message['time'] = time.time()

    dt = datetime.fromtimestamp(message['time'])
    dt_formatted = dt.strftime('%Y/%m/%d %H:%M:%S')

    return f'{username}: {text.strip()}  --- {dt_formatted}'
