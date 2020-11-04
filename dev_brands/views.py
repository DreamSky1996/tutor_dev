from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dev_brands_index(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request,template_name='brands/index.html',context=context)
