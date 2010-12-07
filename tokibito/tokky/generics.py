from google.appengine.ext import webapp

class TemplatePageHandler(webapp.RequestHandler):
    template_name = ''

    def get(self):
        from google.appengine.ext.webapp import template
        self.response.out.write(template.render(self.template_name, self.get_context()))

    def get_context(self):
        return {}
