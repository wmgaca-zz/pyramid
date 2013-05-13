from lib.types.controller import Controller
from lib.utils.rendering import render_to

class MainController(Controller):

    @render_to()
    def index(request):
        return 'Hello, World!'

    @render_to('main')
    def helloworld(request):
        return 'Foo, bar'
