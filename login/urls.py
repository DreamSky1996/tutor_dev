from django.urls import path
from . import views

urlpatterns = [
    path('manage', views.dev_mng_login_staff, name='dev_mng_login_staff'),
    path('member', views.dev_mng_login_member, name='dev_mng_login_member'),
    path('forgotpassword', views.forgot_pwd, name='forgot_password'),
    path('authenticate_staff', views.check_staff, name='auth_staff'),
    path('authenticate_member', views.check_member, name='auth_member'),
]