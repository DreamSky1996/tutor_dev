from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_mng_registration, name='dev_registration'),
    path('continued', views.dev_mng_reg_continued, name='dev_reg_continued'),
    path('success', views.dev_mng_reg_success, name='dev_reg_success'),
    path('get_states', views.get_states, name='get_states'),
]