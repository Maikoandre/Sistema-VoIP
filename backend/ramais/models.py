from django.db import models

class Extension(models.Model):
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.number