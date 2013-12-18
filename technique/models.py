from django.forms import ModelForm
from neo4django.db import models

class Technique(models.NodeModel):
    name = models.StringProperty()  
    category = models.StringProperty()
    image = models.StringProperty()
    start = models.Relationship('self',
            single=True,
            rel_type = 'technique',
            related_name = 'starts_from'
            )



class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        exclude = ['starts_from']
