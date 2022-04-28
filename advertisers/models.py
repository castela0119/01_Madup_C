from django.db import models

# Create your models here.

class Client(models.Model):
    class Meta:
        db_table = 'client'

    name = models.CharField(max_length=100)