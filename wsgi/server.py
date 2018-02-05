__author__ = 'mocy'
#coding:UTF-8
from wsgiref.simple_server import make_server
# 自己编写的application()函数:
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = r'<h1>Hello, %s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
httpd = make_server('',8000,application)
print('server is running')
httpd.serve_forever()