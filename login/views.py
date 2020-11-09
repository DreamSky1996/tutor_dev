import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, views, models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from registration.models import Staffs, Brands, Creators, Roles
# Create your views here.

def dev_mng_login_staff(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request, template_name='loginandregistration/login_staff.html',context=context)

def dev_mng_login_member(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request, template_name='loginandregistration/login_member.html',context=context)

def forgot_pwd(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request, template_name='loginandregistration/forgotpassword.html',context=context)

def check_member(request):
    role = request.POST.get('role', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    try:
        uuser = User.objects.get(email = email)
    except django.contrib.auth.models.User.DoesNotExist:
        if int(role) == 3:
            try:
                member = Brands.objects.get(phone = email)
            except Brands.DoesNotExist:
                return redirect('dev_mng_login_member')
            else:
                member_email = member.email
                member_role = Roles.objects.get(id=member.roles).login_value
        elif int(role) == 4:
            try:
                member = Creators.objects.get(phone = email)
            except Creators.DoesNotExist:
                return redirect('dev_mng_login_member')
            else:
                member_email = member.email
                member_role = Roles.objects.get(id=member.roles).login_value
        try:
            uuser = User.objects.get(email = member_email)
        except django.contrib.auth.models.User.DoesNotExist:
            return redirect('dev_mng_login_member')
        else:
            if uuser.check_password(password) and int(member_role) == int(role):
                login(request, uuser)
                if int(role) == 3:
                    return redirect('dev_brands_index')
                elif int(role) == 4:
                    return redirect('dev_creators_index')
                else:
                    return redirect('dev_mng_login_member')    
            else:
                return redirect('dev_mng_login_member')
    else:
        if int(role) == 3:
            try:
                member = Brands.objects.get(email = email)
            except Brands.DoesNotExist:
                return redirect('dev_mng_login_member')
            else:
                member_role = Roles.objects.get(id=member.roles).login_value
        elif int(role) == 4:
            try:
                member = Creators.objects.get(email = email)
            except Creators.DoesNotExist:
                return redirect('dev_mng_login_member')
            else:
                member_role = Roles.objects.get(id=member.roles).login_value
        print(member_role)
        if uuser.check_password(password) and int(member_role) == int(role):
            login(request, uuser)
            if int(role) == 3:
                return redirect('dev_brands_index')
            elif int(role) == 4:
                return redirect('dev_creators_index')
            else:
                return redirect('dev_mng_login_member')
        else:
            return redirect('dev_mng_login_member')

def check_staff(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    try:
        uuser = User.objects.get(email = email)
    except django.contrib.auth.models.User.DoesNotExist:
        try:
            staff_email = Staffs.objects.get(phone = email).email
        except django.contrib.auth.models.User.DoesNotExist:
            return redirect('dev_mng_login_staff')
        else:
            try:
                uuser = User.objects.get(email = staff_email)
            except django.contrib.auth.models.User.DoesNotExist:
                return redirect('dev_mng_login_staff')
            else:
                if (uuser.check_password(password)):
                    login(request, uuser)
                    return redirect('dev_manage_index')
                else:
                    return redirect('dev_mng_login_staff')
    else:
        is_super = uuser.is_superuser
        if (is_super == 1):
            if (uuser.check_password(password)):
                login(request, uuser)
                return redirect('dev_manage_index')
            else:
                return redirect('dev_mng_login_staff')
        else:
            if uuser.check_password(password):
                login(request, uuser)
                return redirect('dev_manage_index')
            else:
                return redirect('dev_mng_login_staff')

        
        