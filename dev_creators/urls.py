from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_creators_index, name='dev_creators_index'),
]