from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    # TODO: add image field
    # TODO: add options field (e.g. sizes, color, etc.)

    def __str__(self):
        return self.name