from django.forms import ModelForm
from neo4django.db import models

# TODO need a category class apparently 
COLORS = {
        "Submission": "#B90C0D",
        "Sweep": "#0A940A",
        "Position": "#00196A"
    }

DISTANCE = {
        "Submission": 75,
        "Sweep": 150,
        "Position": 75
    }

STRENGTH = {
        "Submission": 1,
        "Sweep": 5,
        "Position": 1
    }

CHARGE = {
        "Submission": -300,
        "Sweep": -300,
        "Position": -300
    }

class Technique(models.NodeModel):
    name = models.StringProperty()  
    category = models.StringProperty()
    image = models.StringProperty()
    start = models.Relationship('self',
            single=True,
            rel_type = 'technique_starts',
            related_name = 'starts_from'
            )

    end = models.Relationship('self',
            single=True,
            rel_type = 'technique_ends',
            related_name = 'ends_at'
            )

    def render_to_json(self):
        return {'pk': self.pk, 'name': self.name, 'category': self.category, 'image': self.image, 'color': COLORS[self.category], 'charge': CHARGE[self.category]}

    def render_links_to_json(self):
        links = []
        if self.start:
            links.append({'source': self.start.pk, 'target': self.pk, 'strength': STRENGTH[self.category], 'distance': 75, 'class': 'link'})
        if self.end:
            links.append({'source': self.pk, 'target': self.end.pk, 'strength': STRENGTH[self.category], 'distance': DISTANCE[self.category], 'class': 'link'})
        if self.start and self.end:
            links.append({'source': self.start.pk, 'target': self.end.pk, 'strength': 0.1, 'distance': DISTANCE[self.category]*2, 'class': 'virtual'})
        return links


class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        exclude = ['starts_from']
