__author__ = 'raphael'

import json


class Answer:
    def on_get(self, req, resp):
        """handles GET request"""
        answer = [42]
        resp.body = json.dumps(answer)

    def __init__(self):
        return
