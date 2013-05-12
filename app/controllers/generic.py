
class ErrorPageController(object):

    @classmethod
    def error404(cls, request):
        return 'Error 404 -- page not found'
