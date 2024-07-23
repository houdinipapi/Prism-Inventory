from django.db import models

# Create your models here.
class Wine(models.Model):
    name= models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name