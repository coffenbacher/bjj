from neo4django.db import models

class Match(models.NodeModel):
    name = models.StringProperty()
