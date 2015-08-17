import json


class Info:
    @staticmethod
    def on_get(req, resp):
        """Handles GET requests"""
        quote = {
            'author': 'Raphael Lehmann',
            'info': 'This ist the ApiInfo from api'
        }

        resp.body = json.dumps(quote)

    def __init__(self):
        return
