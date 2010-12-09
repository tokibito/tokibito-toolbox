from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms

from apps.presentation.models import Presentation

class PresentationModelForm(djangoforms.ModelForm):
    class Meta:
        model = Presentation
