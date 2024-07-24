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
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.pk:
            original = OutletWine.objects.get(pk=self.pk)
            difference = self.quantity - original.quantity
            self.wine.quantity -= difference
        else:
            self.wine.quantity -= self.quantity

        self.wine.save()
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.wine.quantity += self.quantity
        self.wine.save()
        super().delete(*args, **kwargs)

    # class Meta:
    #     unique_together = ('outlet', 'wine')

    def __str__(self):
        return f"{self.outlet.name} - {self.wine.name}"