import sys

def load_application(name):
    bits = name.split('.')
    module_name = '.'.join(bits[:-1])
    app_name = bits[-1]
    __import__(module_name, {}, {}, [])
    module = sys.modules[module_name]
    return getattr(module, app_name)
