from google.appengine.api import memcache

CACHEKEY_PRESENATAION_ALL = 'app.presentation.cache.all'
CACHEKEY_PRESENATAION = 'app.presentation.cache.object_%s'

def get_presentation_all(use_cache=True, cache_timeout=600):
    if use_cache:
        objects = memcache.get(CACHEKEY_PRESENATAION_ALL)
    else:
        objects = None
    if not objects:
        from apps.presentation.models import Presentation
        objects = Presentation.all().order('-created_at')
        memcache.add(CACHEKEY_PRESENATAION_ALL, objects, cache_timeout)
    return objects

def get_presentation(slug, use_cache=True, cache_timeout=3600):
    cache_key = CACHEKEY_PRESENATAION % slug
    if use_cache:
        objects = memcache.get(cache_key)
    else:
        objects = None
    if not objects:
        from apps.presentation.models import Presentation
        from tokky.misc.query import get_by_slug
        obj = get_by_slug(Presentation, slug)
        memcache.add(cache_key, obj, cache_timeout)
    return objects
