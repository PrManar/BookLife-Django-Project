from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products/')
  available = models.BooleanField(default=True)
