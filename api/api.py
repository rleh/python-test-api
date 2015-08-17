import falcon
import info
import answer
import mytime
from wsgiref import simple_server


api = falcon.API()
api.add_route('/info', info.Info())
api.add_route('/answer', answer.Answer())
api.add_route('/time', mytime.Mytime())

# Useful for debugging problems in your API; works with pdb.set_trace()
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
