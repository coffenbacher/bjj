from django.contrib.admin.widgets import FilteredSelectMultiple
from django.conf import settings
from neo4django.db import models
from technique.models import *
from django.forms import ModelForm
from django.forms.widgets import *

# Create your models here.

class Flow(models.NodeModel):
    name = models.StringProperty()
    techniques = models.Relationship(Technique,
            rel_type='flow',
            related_name='flows'
            )

class FlowForm(ModelForm):
    filter_horizontal = ('techniques',)

    class Meta:
        model = Flow
        widgets = {
            'techniques': FilteredSelectMultiple("Techniques", is_stacked=False),
        }

    class Media:
        css = { 'all': (settings.STATIC_URL + 'admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)
