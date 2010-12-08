import os
import sys
import logging

from google.appengine.ext.webapp import util, Request

import config
from tokky.exceptions import Http404

_url_map = []
_setup_syspath = None

def setup_syspath():
    from tokky.directory import get_base_dir
    sys.path = [os.path.join(get_base_dir(), 'library.zip')] + sys.path

def _init_url_map():
    # initialize url mapping
    import re
    global _url_map
    patterns = []
    for pattern, app in config.APPS:
        patterns.append([re.compile(pattern), app])
    _url_map = patterns

def get_traceback(exc_info):
    import traceback
    ret = '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
    try:
        return ret.decode('utf-8')
    except UnicodeDecodeError:
        return ret

def apply_middleware(app):
    from tokky.loader import load_module
    for middleware_name in config.MIDDLEWARE:
        middleware = load_module(middleware_name)
        app = middleware(app)
    return app

def application(environ, start_response):
    # entry point
    global _url_map
    if not _url_map:
        _init_url_map()
    request = Request(environ)
    match_app = ''
    for regexp, app in _url_map:
        if regexp.match(request.path):
            match_app = app
            break
    else:
        # no match patterns.
        raise Http404

    # select app
    from tokky.loader import get_application
    real_app = get_application(match_app)
    # run app
    return real_app(environ, start_response)

_application = None

def main():
    # logging exception
    try:
        global _setup_syspath, _application

        if not _setup_syspath:
            logging.info("sys.path setup.")
            setup_syspath()
            _setup_syspath = True
        if not _application:
            logging.info("application was spinned up.")
            _application = apply_middleware(application)
        util.run_wsgi_app(_application)
    except Exception, e:
        logging.error(get_traceback(sys.exc_info()))
        raise

if __name__ == '__main__':
    main()
