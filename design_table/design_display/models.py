from django.db import models

# Create your models here.

class CurrentImage(models.Model):
    url = models.CharField(max_length=500)
    def __str__(self):
        return self.url