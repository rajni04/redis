from django.db import models

# Create your models here.

class Fruits(models.Model):
    fruits_name=models.CharField(max_length=50)
