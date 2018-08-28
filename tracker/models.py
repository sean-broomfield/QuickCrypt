from django.db import models


# Create your models here.
class Cryptocoin(models.Model):
    rank = models.IntegerField(unique=True, blank=False)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="")
    changehour = models.FloatField(default=0)
    changeday = models.FloatField(default=0)
    changeweek = models.FloatField(default=0)
    price = models.FloatField(default=0.00)
    cap = models.IntegerField(default=0)
    url = models.URLField(default="")

    def __str__(self):
        return self.name