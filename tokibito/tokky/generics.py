from google.appengine.ext import webapp

class TemplatePageHandler(webapp.RequestHandler):
    template_name = ''

    def get(self, *args, **kwargs):
        result = self.render(*args, **kwargs)
        self.response.out.write(result)

    def pre_render(self, *args, **kwargs):
        pass

    def get_context(self, *args, **kwargs):
        return {}

    def get_pathprefix(self):
        return self.request.environ.get('PATH_PREFIX') or ''

    def render(self, *args, **kwargs):
        from google.appengine.ext.webapp import template
        self.pre_render(*args, **kwargs)
        context = {
            'path_prefix': self.get_pathprefix(),
        }
        context.update(self.get_context(*args, **kwargs))
        return template.render(self.template_name, context)
