from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.name