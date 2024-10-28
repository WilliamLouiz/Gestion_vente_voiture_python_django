# noinspection PyUnresolvedReferences
from django.db import models

class Client (models.Model):
    NumClient= models.IntegerField(primary_key = True, null = False, default= 1)
    NomClient= models.CharField(max_length=200, null=True, default= "Michel")
    AdrClient= models.CharField(max_length=200,null=True, default="Menabe")



