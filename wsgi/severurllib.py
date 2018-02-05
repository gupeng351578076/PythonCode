__author__ = 'mocy'
#coding:UTF-8
from urllib import parse
from wsgiref.simple_server import make_server

def application(environ,start_response):
    qstr = environ.get("QUERY_STRING")
    print(qstr)
    print(parse.parse_qs(qstr))
    print(parse.parse_qsl(qstr))
    html = "<h1>重庆欢迎你</h1>"
    start_response("200 OK",[('Content-type','text/plain;charset=utf-8')])
    return [html.encode()]
ip = '127.0.0.1'
port = 9999
server = make_server(ip,port,application)
server.serve_forever()


