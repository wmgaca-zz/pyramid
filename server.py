import SocketServer

from lib.controllers import ErrorPageController
from app.config.routing import routes


def get_contoller_for_request(request_data):
    rdata = request_data.split('\r\n')
    for line in rdata:
        if line.startswith('GET'):
            path = line.split()[1].strip()
            print 'path=%s' % path
            if path in routes:
                return routes[path]

    return ErrorPageController.error404


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        controller = get_contoller_for_request(self.data)
        print 'controller=%s' % controller
        response = controller(self.data)
        print 'output=%s' % response
        self.request.sendall(response)


def run_server():
    host, port = 'localhost', 8080
    server = SocketServer.TCPServer((host, port), MyTCPHandler)
    print '>>> listening on %s:%s' % (host, port)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
