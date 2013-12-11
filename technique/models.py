from neo4django.db import models

class Technique(models.NodeModel):
    name = models.StringProperty()  
    category = models.StringProperty()
    start = models.Relationship('self',
            single=True,
            rel_type = 'technique',
            related_name = 'starts_from'
            )
