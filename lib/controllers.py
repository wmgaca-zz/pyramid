from lib.controller import Controller
from lib.render import render_to

class ErrorPageController(Controller):

    @render_to()
    def error404(request):
        return 'Error 404 -- page not found'
