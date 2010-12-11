# installed apps
APPS = [
    ('^/$', 'apps.toppage.application'),
    ('^/presentation/', 'apps.presentation.handlers.application'),
    ('^/test\.html$', 'apps.pages.application'),
]

# global middleware
MIDDLEWARE = [
    'tokky.middleware.not_found_middleware',
]

# not found app
NOT_FOUND_APP = 'tokky.defaultapps.not_found'

MEDIA_URL = '/'
