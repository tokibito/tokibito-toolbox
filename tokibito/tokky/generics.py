from google.appengine.ext import webapp

class TemplatePageHandler(webapp.RequestHandler):
    template_name = ''

    def get(self):
        result = self.render()
        self.response.out.write(result)

    def pre_render(self):
        pass

    def get_context(self):
        return {}

    def render(self):
        from google.appengine.ext.webapp import template
        self.pre_render()
        return template.render(self.template_name, self.get_context())
