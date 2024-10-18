from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Clothing(models.Model):
    class Meta:
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothes'

    SIZES_CHOICES = [
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
        ('XG', 'XG'),
    ]
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    mark = models.ForeignKey(Mark, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=2, choices=SIZES_CHOICES)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.size} ({self.color})"