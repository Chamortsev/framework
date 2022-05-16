from wsgiref.simple_server import make_server
from main import MyFramework
from urls import routes


with make_server('', 8081, MyFramework(routes)) as httpd:
    print('Сервер запущен...')
    httpd.serve_forever()
