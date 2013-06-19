# coding: utf-8

from lib.types.controller import Controller
from lib.utils.rendering import render_to

class ErrorPageController(Controller):

    @render_to()
    def error404(request):
        return 'Error 404 -- page not found'
