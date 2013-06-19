# coding: utf-8

import os
import unittest
import sys
sys.path.append(os.getcwd())
from lib.utils import twigparser


class TwigParserTestCase(unittest.TestCase):

    def test_parser_compile(self):
        tests = {
            'Hello {{ world }},{{foo}}, {{bar     }}': 'Hello {world},{foo}, {bar}'
        }

        for test_case, expected_result in tests.items():
            result = twigparser.compile_template(test_case)

            self.assertEqual(result, expected_result)

    def test_parser_read(self):
        for template_name in ['default', 'main']:
            result = twigparser.parse(template_name)
            print result


if __name__ == '__main__':
    unittest.main()
