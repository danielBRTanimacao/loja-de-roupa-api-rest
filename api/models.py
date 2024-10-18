from django.db import models

# Create your models here.
class Clothing(models.Model):
    class Meta:
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothes'

    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=3, decimal_places=2)