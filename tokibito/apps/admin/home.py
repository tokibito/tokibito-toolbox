# coding: utf-8
from tokky.generics import TemplatePageHandler

from apps.admin.handlers import AdminApp

class AdminHomePageHandler(TemplatePageHandler):
    template_name = 'templates/admin/home.html'

    def get_context(self, *args, **kwargs):
        admin_menu = []
        for app in self.admin_site.apps:
            if app.index_path:
                admin_menu.append({
                    'name': app.name,
                    'path': app.index_path,
                })
        return {'admin_menu': admin_menu}

application = webapp.WSGIApplication([(r'/', AdminHomePageHandler)])

class AdminHome(AdminApp):
    name = u'ÉzÅ[ÉÄ'

    def __call__(self, environ, start_response):
        return application(environ, start_response)
