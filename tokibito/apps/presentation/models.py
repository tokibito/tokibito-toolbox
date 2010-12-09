from google.appengine.ext import db

class Presentation(db.Model):
    """
    Presentation model
    """
    title = db.StringProperty(required=True, multiline=False)
    body = db.TextProperty(required=True)
    slug = db.StringProperty(required=True, multiline=False)
    created_at = db.DateTimeProperty(auto_now_add=True)

