from lib.controller import Controller
from lib.render import render_to

class MainController(Controller):

    @render_to()
    def index(request):
        return 'Hello, World!'

    @render_to('main')
    def helloworld(request):
        return 'Foo, bar'
