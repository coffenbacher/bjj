from neo4django.db import models
from technique.models import *

# Create your models here.

class Flow(models.NodeModel):
    name = models.StringProperty()
    techniques = models.Relationship(Technique,
            rel_type='flow',
            related_name='flows'
            )
