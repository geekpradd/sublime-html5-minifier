# -*- coding: utf-8 -*-

from .parser import Parser


def minify(html, **kwargs):
    minifier = Minifier(**kwargs)
    return minifier.minify(html)


class Minifier(object):

    def __init__(self, **kwargs):
        self._parser = Parser(**kwargs)

    def minify(self, html):
        self._parser.feed(html)
        self._parser.close()
        result = self._parser.get_minified_html()
        self._parser.reset()
        return result
