# coding: utf-8

import os
import re
from lib.utils import cache

_base_template_path = os.path.join(os.getcwd(), 'app/templates')
_var_pattern = re.compile(r'({{\s*(\w+)\s*}})')


def _get_template_path(template_name):
    return os.path.join(_base_template_path, '%s.html.twig' % template_name)


def _read_template(template_name):
    path = _get_template_path(template_name)

    with open(path, 'rb') as f:
        return f.read()


def compile_template(template_contents):
    """Parses simple twig.
    """

    result = []
    last = 0

    for found in re.finditer(_var_pattern, template_contents):
        result.append(template_contents[last:found.start()])
        result.append('{%s}' % found.group()[2:-2].strip())
        last = found.end()

    result.append(template_contents[last:])

    return ''.join(result)


def parse(template_name):
    if cache.is_stored(template_name):
        return cache.get(template_name)
    else:
        compiled = compile_template(_read_template(template_name))
        cache.put(template_name, compiled)
        return compiled