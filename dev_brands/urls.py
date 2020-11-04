from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_brands_index, name='dev_brands_index'),
]