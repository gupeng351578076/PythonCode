__author__ = 'mocy'
#coding:UTF-8
from wsgiref.simple_server import make_server
def demo_app(environ,start_response):
    from io import StringIO
    stdout = StringIO()
    print("hello world",file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k,v in h:
        print(k,repr(v),file=stdout)
    start_response("200 OK",[('Content-type','text/plain;charset=utf-8')])
    return [stdout.getvalue().encode('utf-8')]
ip = '127.0.0.1'
port = 9999
server = make_server(ip,port,demo_app)
server.serve_forever()
