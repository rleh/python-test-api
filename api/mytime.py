import time
import json


class Mytime:
    def on_get(self, req, resp):
        quote = {
            'time': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        }
        resp.body = json.dumps(quote)

    def __init__(self):
        return
