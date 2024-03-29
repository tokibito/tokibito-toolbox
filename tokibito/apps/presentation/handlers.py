from google.appengine.ext import webapp

from tokky.generics import TemplatePageHandler

from apps.presentation_redirects import presentation_redirects_middleware

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
        obj = api.get_presentation(slug=slug)
        if not obj:
            from tokky.exceptions import Http404
            raise Http404
        return {'object': obj}


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


application = presentation_redirects_middleware(webapp.WSGIApplication([
    (r'/(.*)\.html', PresentationPageHandler),
    (r'/create', PresentationCreateHandler),
]))
