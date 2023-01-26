from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_suite, name='dishes'),
    path('groceries', views.groceries, name='groceries')

]
