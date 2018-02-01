from django.db import models

from owners.models import Owner


class Animal(models.Model):
    name = models.CharField('Pet name', max_length=50)
    breed = models.CharField('Breed',max_length=30)
    age = models.IntegerField('Age', default=0)
    sound = models.CharField('Sound',max_length=10)
    owner = models.ForeignKey(Owner, models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        return f"The {self.name} says {self.sound}"
