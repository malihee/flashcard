from statistics import mode
from django.db import models


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    vocab = models.CharField(max_length=50)
    pronuns = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    translation = models.TextField(blank=True)
    memorized = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
