from lib.render import render_to

class MainController(object):

    @classmethod
    @render_to('main')
    def index(self, request):
        return 'Hello, World!'

    @classmethod
    @render_to('main')
    def helloworld(self, request):
        return 'Foo, bar'
