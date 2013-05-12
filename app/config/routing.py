from app.controllers.main import *

routes = {

    '/': MainController.index,
    
    '/hello/world': MainController.helloworld

}
