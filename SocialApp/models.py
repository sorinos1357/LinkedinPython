from django.db import models

# Create your models here.

class Test(models.Model):
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)