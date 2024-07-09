from django.db import models

# Create your models here.

class BookTable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=155)
    number = models.CharField(max_length=15)
    date = models.DateField()
