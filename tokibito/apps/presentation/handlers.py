from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

class PresentationPageHandler(TemplatePageHandler):
    template_name = 'templates/presentation/page.html'

    def pre_render(self, *args, **kwargs):
        from google.appengine.ext.webapp import template
        import docutils
        from apps.presentation import pygments_support
        from docutils.core import publish_parts
        template.register_template_library('apps.presentation.templatetags.s6helper')

    def get_context(self, slug):
        from apps.presentation import api
        return {'object': api.get_presentation(slug=slug)}


class PresentationCreateHandler(TemplatePageHandler):
    template_name = 'templates/presentation/create.html'

    def get_context(self):
        from apps.presentation.forms import PresentationModelForm
        form = PresentationModelForm()
        return {'form': form}

    def post(self):
        from apps.presentation.forms import PresentationModelForm
        form = PresentationModelForm(self.request.POST)
        if form.is_valid():
            obj = form.save()
            self.redirect(self.get_pathprefix() + obj.slug + '.html')
        else:
            result = self.render(context={'form': form})
            self.response.out.write(result)


application = webapp.WSGIApplication([
    ('/(.*)\.html', PresentationPageHandler),
    ('/create', PresentationCreateHandler),
])
