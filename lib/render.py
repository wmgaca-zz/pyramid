import os


def render_template(template_name, data):
    print template_name, os.getcwd(), data
    with open(os.path.join(os.getcwd(), 'app/templates/%s.html.twig' % template_name)) as f:
        fcontents = f.read()

        fcontents = fcontents.replace('{{ content }}', str(data))

        return fcontents

def render_to(template_name):
    def controller_decorator(controller):
        def controller_wrapper(*args, **kwargs):
            print args, kwargs
            data = controller(*args, **kwargs)
            return render_template(template_name, data)
        return controller_wrapper
    return controller_decorator


