import SocketServer

from app.controllers.generic import ErrorPageController
from app.config.routing import routes


def get_contoller_for_request(request_data):
    rdata = request_data.split('\r\n')
    print rdata
    for line in rdata:
        if line.startswith('GET'):
            path = line.split()[1].strip()
            if path in routes:
                return routes[path]

    return ErrorPageController.error404


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print '%s wrote:' % (self.client_address[0])
        controller = get_contoller_for_request(self.data)
        self.request.sendall(str(controller(self.data)))


def run_server():
    host, port = 'localhost', 8080
    server = SocketServer.TCPServer((host, port), MyTCPHandler)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
