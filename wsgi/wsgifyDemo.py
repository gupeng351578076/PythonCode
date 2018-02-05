__author__ = 'mocy'
#coding:UTF-8
from wsgiref.simple_server import make_server
from webob import Request,Response,dec
@dec.wsgify
def app(request:Request)->Response:
    return Response("<h1>重庆欢迎你</h1>")
if __name__ =="__main__":
    ip='127.0.0.1'
    port=9999
    server = make_server(ip,port,app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()