from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev_mng_login, name='dev_login'),
    path('registration', views.dev_mng_registration, name='dev_registration'),
    path('reg_continued', views.dev_mng_reg_continued, name='dev_reg_continued'),
    path('login_success', views.dev_mng_login_success, name='dev_login_success'),
]