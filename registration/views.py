from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Staffs, Brands, Creators, Roles, CompanySize, CompanyType, ContentCategory, Status, Countries, States
import django.contrib.auth.models
from django_countries import countries
from django.views.decorators.csrf import csrf_exempt
import simplejson
import json
# Create your views here.

@csrf_exempt
def get_states(request):
    country_id = request.POST.get('countryId', None)
    states = States.objects.filter(country_id= country_id)
    state_list = []
    for state in states:
        temp_state = {}
        temp_state['id'] = state.id
        temp_state['name']= state.name
        temp_state['country_id']= state.country_id
        state_list.append(temp_state)
    return HttpResponse(json.dumps(state_list))

def dev_mng_registration(request):
    roles = Roles.objects.all()
    countries = Countries.objects.all()
    context = {
        'countries': countries,
        'roles': roles,
        }
    
    return render(request=request, template_name='loginandregistration/registration.html',context=context)

def dev_mng_reg_continued(request):
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    phone = request.POST.get('phone', None)
    country = request.POST.get('country', None)
    state = request.POST.get('state', None)
    roles = request.POST.get('roles', None)
    
    gender = request.POST.get('gender', None)
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    
    reg_info = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'country': country,
        'state': state,
        'roles': int(roles),
        'gender': gender,
        'username': username,
        'password': password,
    }

    company_size = CompanySize.objects.all()
    company_type = CompanyType.objects.all()
    content_category = ContentCategory.objects.all()

    context = {
        'reg_info': reg_info,
        'company_size': company_size,
        'company_type': company_type,
        'content_category': content_category,
        }
    return render(request=request, template_name='loginandregistration/reg_continued.html',context=context)

def handle_uploaded_file(f, photo_path):
    with open(photo_path + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def dev_mng_reg_success(request):
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    phone = request.POST.get('phone', None)
    country = request.POST.get('country', None)
    state = request.POST.get('state', None)
    roles = request.POST.get('roles', None)
    role_name = Roles.objects.get(id = int(roles)).role_name
    role_value = Roles.objects.get(id = int(roles)).role_value
    photo_path = 'uploads/photo/staffs/'
    if (role_name == "Brand" or role_name == "Advertiser"):
        photo_path = 'uploads/photo/brands/'
    elif (role_name == "Creator" or role_name == "Influencer"):
        photo_path = 'uploads/photo/creators/'
    
    gender = request.POST.get('gender', None)
    username = request.POST.get('username', None)
    password = make_password(request.POST.get('password', None))

    if int(roles) < 5:
        company_name = request.POST.get('company_name', None)
        company_size = request.POST.get('company_size', None)
        company_type = request.POST.get('company_type', None)
    else:
        content_category = request.POST.get('content_category', None)
        birthday = request.POST.get('birthday', None)
    
    email = request.POST.get('email', None)
    photo = "/" + photo_path + request.FILES['photo'].name

    handle_uploaded_file(request.FILES['photo'], photo_path)
    instagram = request.POST.get('instagram', None)
    facebook = request.POST.get('facebook', None)
    twitter = request.POST.get('facebook', None)
    tiktok = request.POST.get('tiktok', None)
    snapchat = request.POST.get('snapchat', None)
    youtube = request.POST.get('youtube', None)
    pin = 1234

    is_staff = 0
    if (int(role_value) == 1 or int(role_value) == 2):
        is_staff = 1
        reg_add = Staffs(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            country = country,
            state = state,
            roles = roles,
            gender = gender,
            username = username,
            password = password,
            company_name = company_name,
            company_size = company_size,
            company_type = company_type,
            email = email,
            photo = photo,
            status = 1,
            instagram = instagram,
            facebook = facebook,
            twitter = twitter,
            tiktok = tiktok,
            snap = snapchat,
            youtube = youtube,
            pin = pin,
        )
        reg_add.save()
    elif (int(role_value) == 3 or int(role_value) == 4):
        reg_add = Brands(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            country = country,
            state = state,
            roles = roles,
            gender = gender,
            username = username,
            password = password,
            company_name = company_name,
            company_size = company_size,
            company_type = company_type,
            email = email,
            photo = photo,
            status = 1,
            instagram = instagram,
            facebook = facebook,
            twitter = twitter,
            tiktok = tiktok,
            snap = snapchat,
            youtube = youtube,
            pin = pin,
        )
        reg_add.save()
    elif (int(role_value) == 5 or int(role_value) == 6):
        reg_add = Creators(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            country = country,
            state = state,
            roles = roles,
            gender = gender,
            username = username,
            password = password,
            content_category = content_category,
            birthday = birthday,
            email = email,
            photo = photo,
            status = 2,
            instagram = instagram,
            facebook = facebook,
            twitter = twitter,
            tiktok = tiktok,
            snap = snapchat,
            youtube = youtube,
            pin = pin,
        )
        reg_add.save()    

    regToAuth = User(
        is_superuser = 0,
        username = username,
        password = password,
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_active = 1,
        is_staff = is_staff
    )
    regToAuth.save()
    return render(request=request, template_name='loginandregistration/success.html')

    
