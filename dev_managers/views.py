from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dev_mng_index(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='manage/index.html',context=context)

def dev_mng_users(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='manage/users.html',context=context)

def dev_mng_staffs(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='manage/staffs.html',context=context)
