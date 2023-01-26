from django.shortcuts import render
from . import models


def first_suite(request):
    meals = models.FoodToMeal.objects.order_by('-published')
    return render(request, 'MySuitCascade/index.html', {'meals': meals})


def groceries(request):
    return render(request, 'MySuitCascade/groserirslist.html')