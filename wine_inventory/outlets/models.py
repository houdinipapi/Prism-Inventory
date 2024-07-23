from django.db import models
from wines.models import Wine

# Create your models here.
class Outlet(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class OutletWine(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('outlet', 'wine')

    def __str__(self):
        return f"{self.outlet.name} - {self.wine.name}"