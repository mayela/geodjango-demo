import uuid

from django.contrib.gis.db import models

from vets.models import Vet


class Hospital(models.Model):
    chief_vet = models.ForeignKey(Vet, models.SET_NULL, blank=True, null=True)
    name = models.CharField('Name', max_length=255)
    address = models.CharField('Address', max_length=255)
    location = models.PointField()
    license = models.UUIDField(default=uuid.uuid4, editable=False)
