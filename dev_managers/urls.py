from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_mng_index, name='dev_manage_index'),
    path('users', views.dev_mng_users, name='dev_manage_users'),
    path('staffs', views.dev_mng_staffs, name='dev_manage_staffs'),
]