# -*- coding: utf-8 -*-
# Copyright (c) 2016, Philip Xu <pyx@xrefactor.com>
# License: BSD New, see LICENSE for details.
"""Flask-SimpleMDE - a Flask extension for SimpleMDE Markdown Editor"""

from flask import Blueprint, Markup, current_app, url_for

__version__ = '0.3.0'
__all__ = ['SimpleMDE']

CDN_PREFIX = '//cdn.jsdelivr.net/simplemde/latest/'

CSS = 'simplemde.min.css'
CSS_LINK_TEMPLATE = '<link rel="stylesheet" href="%s">'
CSS_CDN_LINK = CSS_LINK_TEMPLATE % (CDN_PREFIX + CSS)

JS = 'simplemde.min.js'
JS_LINK_TEMPLATE = '<script src="%s"></script>'
JS_CDN_LINK = JS_LINK_TEMPLATE % (CDN_PREFIX + JS)

JS_LOAD = """<script>
var simplemde = new SimpleMDE();
</script>
"""

JS_LOAD_IIFE = """<script>
(function () {
  var simplemde = new SimpleMDE();
})();
</script>
"""

JS_LOAD_WITH_ID = """<script>
var simplemde = new SimpleMDE({ element: document.getElementById("%s") });
</script>
"""

JS_LOAD_WITH_ID_IIFE = """<script>
(function () {
    var simplemde = new SimpleMDE({ element: document.getElementById("%s") });
})();
</script>
"""

EXTENSION = 'simplemde'
STATIC_ENDPOINT = EXTENSION + '.static'


class SimpleMDE(object):
    """Flask-SimpleMDE extension

    provides links to SimpleMDE's static assets.
    """
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """create and register a blueprint with the Flask application.

        :param app:
            Flask application instance
        """
        app.config.setdefault('SIMPLEMDE_JS_IIFE', True)
        app.config.setdefault('SIMPLEMDE_USE_CDN', True)

        simplemde = Blueprint(
            EXTENSION,
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + '/' + EXTENSION)

        app.register_blueprint(simplemde)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions[EXTENSION] = self
        app.context_processor(lambda: {EXTENSION: self})

    @property
    def css(self):
        """property that will be rendered as :code:`<link>` tags for css"""
        if current_app.config['SIMPLEMDE_USE_CDN']:
            link = CSS_CDN_LINK
        else:
            link = CSS_LINK_TEMPLATE % url_for(STATIC_ENDPOINT, filename=CSS)

        return Markup(link)

    @property
    def js(self):
        """property that will be rendered as :code:`<style>` tags for js"""
        if current_app.config['SIMPLEMDE_USE_CDN']:
            link = JS_CDN_LINK
        else:
            link = JS_LINK_TEMPLATE % url_for(STATIC_ENDPOINT, filename=JS)

        return Markup(link)

    @property
    def load(self):
        """property that will be rendered as javascript loading code"""
        if current_app.config['SIMPLEMDE_JS_IIFE']:
            code = JS_LOAD_IIFE
        else:
            code = JS_LOAD
        return Markup(code)

    def load_id(self, id):
        """method that renders javascript loading code for specific id"""
        if current_app.config['SIMPLEMDE_JS_IIFE']:
            code = JS_LOAD_WITH_ID_IIFE
        else:
            code = JS_LOAD_WITH_ID
        return Markup(code % id)
