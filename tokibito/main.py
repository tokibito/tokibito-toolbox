import logging
import sys

from google.appengine.ext.webapp import util, Request

import config
from tokky.exceptions import Http404

# application cache variable
_app_cache = {}


def get_traceback(exc_info):
    import traceback
    ret = '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
    try:
        return ret.decode('utf-8')
    except UnicodeDecodeError:
        return ret


def get_application(name):
    global _app_cache
    from tokky.loader import load_application
    if name in _app_cache:
        app = _app_cache[name]
    else:
        app = load_application(name)
        _app_cache[name] = app
    return app


def not_found_middleware(app):
    def _inner(environ, start_response):
        try:
            return app(environ, start_response)
        except Http404, e:
            not_found_app = get_application(config.NOT_FOUND_APP)
            return not_found_app(environ, start_response)
    _inner.__func__ = app
    return _inner


@not_found_middleware
def application(environ, start_response):
    # entry point
    request = Request(environ)
    match_app = ''
    for prefix, app in config.APPS:
        if request.path.startswith(prefix):
            match_app = app
            break
    else:
        # no match patterns.
        raise Http404

    # select app
    real_app = get_application(match_app)
    # run app
    return real_app(environ, start_response)


def main():
    # logging exception
    try:
        util.run_wsgi_app(application)
    except Exception, e:
        logging.error(get_traceback(sys.exc_info()))
        raise


if __name__ == '__main__':
    main()
