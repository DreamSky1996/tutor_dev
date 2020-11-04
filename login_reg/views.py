from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dev_mng_login(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='loginandregistration/login.html',context=context)

def dev_mng_registration(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='loginandregistration/registration.html',context=context)

def dev_mng_reg_continued(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='loginandregistration/reg_continued.html',context=context)

def dev_mng_login_success(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='loginandregistration/success.html',context=context)
