__author__ = 'mocy'
#coding:UTF-8
from wsgiref.simple_server import make_server
from webob import Request,Response
def application(environ:dict,start_response):
    request = Request(environ)
    print(request.method)
    print(request.path)
    print(request.GET)
    print(request.POST)
    print(request.params)
    print(request.query_string)
    html = '<h1>重庆欢迎你</h1>'
    start_response("200 OK",[('Content-type','text/plain;charset=utf-8')])
    return [html.encode()]
ip = '127.0.0.1'
port = 9999
server = make_server(ip,port,application)
server.serve_forever()