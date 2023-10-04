from django.db import models

class Things(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
