# noinspection PyUnresolvedReferences
from django.db import models
from client.models import Client
from voiture.models import Voiture

# Create your models here.
class Vente (models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default= 1)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, default= 1 )
    DateVente = models.DateTimeField(auto_now_add = True,null = True)

