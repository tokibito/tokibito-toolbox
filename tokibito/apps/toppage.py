from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

class TopPageHandler(TemplatePageHandler):
    template_name = 'templates/index.html'

application = webapp.WSGIApplication([('/', TopPageHandler)])
