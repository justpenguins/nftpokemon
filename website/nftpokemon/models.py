from django.db import models

# Create your models here.
class NFT(models.Model):
    name = models.CharField(max_length=200)
    token = models.IntegerField()
    img = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)