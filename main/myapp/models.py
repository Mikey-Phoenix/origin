from django.db import models

# Create your models here.

class ArtWork(models.Model):
    # number = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=200)
    hot = models.BooleanField(default=False)
    initialBid = models.FloatField(max_length=3)
    art_description = models.CharField(max_length=5000)
    art_image = models.ImageField(null=True, blank=True, upload_to="images/")

class Bid(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    bid = models.FloatField(max_length=10)