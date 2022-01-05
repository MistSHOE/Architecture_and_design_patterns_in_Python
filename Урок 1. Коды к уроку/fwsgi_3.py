from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(type(environ))
    print(environ)
    path = environ['PATH_INFO']
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index 1000']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC 5000']
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [b'404 Not Found error']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
