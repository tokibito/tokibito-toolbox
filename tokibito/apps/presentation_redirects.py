import re

redirect_url_mapping = {
  '/1/': '/presentation/isk-daemon.html',
  '/2/': '/presentation/ruby-sapporo-django.html',
  '/3/': '/presentation/bpstudy-django-admin.html',
  '/4/': '/presentation/django-hack-a-thon-contenttypes.html',
  '/5/': '/presentation/osc-2009-hokkaido-django.html',
  '/8/': '/presentation/appengine-ja-night-rst2pdf.html',
  '/9/': '/presentation/bpstudy37-django-useful.html',
}

def presentation_redirects_middleware(application):
    # redirect from old url.
    def _application(environ, start_response):
        path = environ.get('PATH_INFO')
        import logging
        logging.info(path)
        redirect_url = redirect_url_mapping.get(path)
        if redirect_url:
            scheme = environ['wsgi.url_scheme']
            host = environ['HTTP_HOST']
            start_response(
                '301 Moved Permanently',
                [('Location', '%s://%s%s' % (scheme, host, redirect_url))]
            )
            return '301 Moved Permanently'
        return application(environ, start_response)
    return _application
