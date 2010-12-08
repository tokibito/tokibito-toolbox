from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

class TopPageHandler(TemplatePageHandler):
    template_name = 'templates/test.html'

    def pre_render(self):
        from google.appengine.ext.webapp import template
        import docutils
        from docutils.core import publish_parts
        template.register_template_library('django.contrib.markup.templatetags.markup')

    def get_context(self):
        return {
            'text': """
test
====

- spam
- egg
"""
        }

application = webapp.WSGIApplication([('/.*', TopPageHandler)])
