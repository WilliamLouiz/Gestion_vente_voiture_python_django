# noinspection PyUnresolvedReferences
from django.db import models

# Create your models here.
class Voiture (models.Model):
    Marque = models.CharField(max_length = 200, null = True)
    Pu = models.FloatField(null = True)
    Matricule = models.CharField(max_length=20, primary_key=True, null = False, default= 1)
    image = models.ImageField(upload_to='voiture_images/', null=True, blank=True)