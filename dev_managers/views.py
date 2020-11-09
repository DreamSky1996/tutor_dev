from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Staffs, Roles, Status, CompanySize, CompanyType, Brands, Creators
# Create your views here.

def dev_mng_index(request):
    active = {
        'home': 'active',
    }
    context = {
        'active': active
        }
    return render(request=request, template_name='manage/index.html', context=context)

def dev_mng_users(request):
    brands = Brands.objects.all()
    creators = Creators.objects.all()

    for brand in brands:
        brand.roles = Roles.objects.get(id = brand.roles).role_name
        brand.company_size = CompanySize.objects.get(id=brand.company_size).company_size
        brand.company_type = CompanyType.objects.get(id=brand.company_type).company_type
        brand.status = Status.objects.get(id=brand.status).status
    
    for creator in creators:
        creator.roles = Roles.objects.get(id = creator.roles).role_name
        creator.company_size = CompanySize.objects.get(id=creator.company_size).company_size
        creator.company_type = CompanyType.objects.get(id=creator.company_type).company_type
        creator.status = Status.objects.get(id=creator.status).status

    context = {
        'brands': brands,
        'creators': creators,
        }
    
    return render(request=request, template_name='manage/users.html', context=context)

def dev_mng_staffs(request):
    staffs = Staffs.objects.all()
    for staff in staffs:
        staff.roles = Roles.objects.get(id = staff.roles).role_name
        staff.company_size = CompanySize.objects.get(id=staff.company_size).company_size
        staff.company_type = CompanyType.objects.get(id=staff.company_type).company_type
        staff.status = Status.objects.get(id=staff.status).status
    
    context = {
        'staffs': staffs
        }
    return render(request=request, template_name='manage/staffs.html', context=context)
