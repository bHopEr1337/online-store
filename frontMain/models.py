from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f"Название: {self.name}"


class User_feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    text_body = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User,
    #                            on_delete=models.CASCADE,
    #                            related_name='user_feedback')

    def __str__(self):
        return f"Запрос от: {self.name}"

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail')
