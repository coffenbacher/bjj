from neo4django.db import models

class Technique(models.NodeModel):
    name = models.StringProperty()  
