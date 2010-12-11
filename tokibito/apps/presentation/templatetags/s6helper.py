import re

from docutils.core import publish_parts

from django import template
from django.template.defaultfilters import stringfilter

re_embed = re.compile('<!--(?P<embed>(.|\r?\n)*?)-->')
scripts_embed = '<script type="text/javascript">\n\g<embed>\n</script>'

register = template.Library()

def smart_encode(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s

def smart_unicode(s):
    return s.decode('utf-8')

@stringfilter
def s6rest(value):
    parts = publish_parts(
        source=smart_encode(value),
        writer_name="html4css1",
        settings_overrides={
            'doctitle_xform': 0,
            'initial_header_level': 1
        }
    )
    return parts["fragment"]

@stringfilter
def s6embed(value):
    return re_embed.sub(scripts_embed, value)

register.filter(s6embed)
register.filter(s6rest)
