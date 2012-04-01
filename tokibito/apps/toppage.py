import sys
import re

from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

RE_UA_SMARTPHONE = re.compile(r'(Android|iPhone)')

class TopPageHandler(TemplatePageHandler):
    template_name = 'templates/index.html'

    def get_context(self, *args, **kwargs):
        from apps.presentation import api as presentation_api
        return {
            'is_smartphone': bool(RE_UA_SMARTPHONE.search(self.request.user_agent)),
            'presentation_objects': presentation_api.get_presentation_all(),
            'sys_version': sys.version,
        }

application = webapp.WSGIApplication([(r'/', TopPageHandler)])
