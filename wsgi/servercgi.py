__author__ = 'mocy'
#coding:UTF-8
from wsgiref.simple_server import make_server
import cgi
def demo_app(environ,start_response):
    qstr = environ.get("QUERY_STRING")
    print(qstr)
    print(cgi.parse_qs(qstr))
    print(cgi.parse_qsl(qstr))
    html = "<h1>重庆欢迎你</h1>"
    start_response("200 OK",[('Content-type','text/plain;charset=utf-8')])
    return [html.encode()]
ip = '127.0.0.1'
port = 9999
server = make_server(ip,port,demo_app)
server.serve_forever()