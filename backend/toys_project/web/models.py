from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  name= models.CharField(max_length=30, unique=True)
  description= models.CharField(max_length=300)
  def __str__(self):
        return f"{self.name}: {self.description}"

class Item(models.Model):
  name = models.CharField(max_length=70)
  price = models.IntegerField()
  last_updated = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)

class Review(models.Model):
  title= models.CharField(max_length=30)
  description= models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE)
  updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)