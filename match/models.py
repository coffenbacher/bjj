from neo4django.db import models
from video.models import Video

class Match(models.NodeModel):
    name = models.StringProperty()
    youtube_id = models.StringProperty() # trying denormalized ids for simplicity

    def image(self):
        return 'http://img.youtube.com/vi/%s/maxresdefault.jpg' % self.youtube_id
