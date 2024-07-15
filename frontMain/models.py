from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f"Название: {self.name}"
