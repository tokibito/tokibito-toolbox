# coding: utf-8
class AdminApp(object):
    name = ''

    def __init__(self, admin_site):
        self._name = self.__class__.name or 'Example Admin'
        self._admin_site =  admin_site

    def get_app_name(self):
        return self._name
    name = property(get_app_name)

    def get_admin_site(self):
        return self._admin_site
    admin_site = property(get_admin_site)

    def get_index_path(self):
        """
        アプリケーションのトップページのパスを返す
        """
    index_path = property(get_index_path)

    def __call__(self, environ, start_response):
        raise NotImplementedError

class AdminSite(object):
    def __init__(self, config=None):
        self._init(config)

    def _init(self, config):
        url_map = []

        # apps list from config
        if issubclass(type(config), dict):
            apps_list = config.get('APPS')
        else:
            apps_list = getattr(config, 'APPS')

        import re
        from tokky.loader import load_module
        for url_pattern, app_handler_name in apps_list:
            regexp = re.compile(url_pattern)
            app_handler = load_module(app_handler_name)
            url_map.append((regexp, app_handler(self)))

        self._url_map = url_map
        self._config = config

    def __call__(self, environ, start_response):
        pass

import config
application = AdminSite(config.ADMIN_SITE)
