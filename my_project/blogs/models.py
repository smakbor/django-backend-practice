from django.db import models

# Create your models here.
class Blog(models.Model):
    bid = models.IntegerField()
    tilte=models.CharField(max_length=30)
    desc = models.CharField(max_length= 100)