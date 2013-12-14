from neo4django.db import models
from technique.models import *

class Video(models.NodeModel):
    youtube_id = models.StringProperty()  
    techniques = models.Relationship(Technique,
            rel_type = 'video',
            related_name='instructionals'
            )
