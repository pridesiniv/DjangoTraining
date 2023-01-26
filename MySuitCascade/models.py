from django.db import models


# Create your models here.

class FoodToMeal(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    published = models.DateField(auto_now_add=True, db_index=True)
    img = models.ImageField(null=True, blank=True)


class GroseriesList(models.Model):
    content = models.TextField(null=True, blank=True)