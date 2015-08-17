import falcon
import info
import answer
from wsgiref import simple_server


api = falcon.API()
api.add_route('/info', info.Info())
api.add_route('/answer', answer.Answer())

# Useful for debugging problems in your API; works with pdb.set_trace()
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
