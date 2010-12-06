from google.appengine.ext import webapp

class TopPageHandler(webapp.RequestHandler):
    def get(self):
        from google.appengine.ext.webapp import template
        self.response.out.write(template.render('templates/index.html', {}))

application = webapp.WSGIApplication([('/', TopPageHandler)])
