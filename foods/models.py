from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_type = models.ForeignKey(FoodType,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    composition = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
