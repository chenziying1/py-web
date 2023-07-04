from django.db import models

# Create your models here.
class message(models.Model):
    text = models.CharField(max_length=128,unique = True)
    date = models.CharField(max_length=20,unique= True)

    def __str__(self):
        return self.text
