from google.appengine.ext import webapp

class TopPageHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('toppage.')

application = webapp.WSGIApplication([('/', TopPageHandler)])
