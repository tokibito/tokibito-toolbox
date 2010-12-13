# installed apps
APPS = [
    (r'^/$', 'apps.toppage.application'),
    (r'^/presentation/', 'apps.presentation.handlers.application'),
]

# global middleware
MIDDLEWARE = [
    'tokky.middleware.not_found_middleware',
]

# not found app
NOT_FOUND_APP = 'tokky.defaultapps.not_found'

MEDIA_URL = '/'
