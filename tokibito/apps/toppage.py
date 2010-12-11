from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

class TopPageHandler(TemplatePageHandler):
    template_name = 'templates/index.html'

    def get_context(self, *args, **kwargs):
        from apps.presentation import api as presentation_api
        return {
            'presentation_objects': presentation_api.get_presentation_all()
        }

application = webapp.WSGIApplication([('/', TopPageHandler)])
