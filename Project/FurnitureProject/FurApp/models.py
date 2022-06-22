from django.db import models

# Create your models here.


class Chair(models.Model):
    img = models.ImageField(upload_to="pics")
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

