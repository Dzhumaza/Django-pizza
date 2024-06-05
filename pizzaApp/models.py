from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    price = models.IntegerField(default=0)
    weight = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.title
