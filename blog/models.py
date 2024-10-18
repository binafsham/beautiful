from django.db import models

# Create your models here.
class Products(models.Model):
        name = models.CharField(max_length=55)
        img = models.ImageField()
        price = models.IntegerField()
        bio = models.TextField()

        def __str__(self):
            return self.name
