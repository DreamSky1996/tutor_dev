import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import models
import django.utils.timezone

# Create your models here.

class Countries(models.Model):
    sortname = models.CharField(max_length=255, verbose_name='sortname')
    name = models.CharField(max_length=255, verbose_name='name')
    phonecode = models.IntegerField(default=1, verbose_name='phonecode')
    class Meta:
        db_table = "countries"

class States(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    country_id = models.IntegerField(default=1, verbose_name='country_id')
    class Meta:
        db_table = "states"

class Roles(models.Model):
    role_name = models.CharField(max_length=255, verbose_name='role_name')
    role_value = models.IntegerField(default=1, verbose_name='role_value')
    login_value = models.IntegerField(default=1, verbose_name='login_value')
    class Meta:
        db_table = "roles"

class CompanySize(models.Model):
    company_size = models.CharField(max_length=255, verbose_name='company_size')
    class Meta:
        db_table = "company_size"

class CompanyType(models.Model):
    company_type = models.CharField(max_length=255, verbose_name='company_type')
    class Meta:
        db_table = "company_type"

class ContentCategory(models.Model):
    category_creator = models.CharField(max_length=255, verbose_name='category_creator')
    category_influencer = models.CharField(max_length=255, verbose_name='category_influencer')
    class Meta:
        db_table = "content_category"

class Status(models.Model):
    status = models.CharField(max_length=255, verbose_name='status')
    class Meta:
        db_table = "status"

class BadgeLevels(models.Model):
    levels = models.IntegerField(default=1, verbose_name='levels')
    badges = models.CharField(max_length=255, verbose_name='badges')
    influencers = models.CharField(max_length=255, verbose_name='influencers')
    content_creators = models.CharField(max_length=255, verbose_name='content_creators')

    class Meta:
        db_table = "badge_levels"

class Staffs(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    #birthday = models.DateField(verbose_name='DOB')
    gender = models.CharField(max_length=50, verbose_name='gender')
    email = models.EmailField(max_length=254, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='phone')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    password = models.CharField(max_length=255, verbose_name='password')
    state = models.CharField(max_length=255, verbose_name='state')
    country = models.CharField(max_length=255, verbose_name='country')
    company_name = models.CharField(max_length=255, verbose_name='company_name')
    company_email = models.EmailField(max_length=254, verbose_name='company_email')
    company_size = models.IntegerField(verbose_name='company_size')
    company_type = models.IntegerField(verbose_name='company_type')
    photo = models.ImageField(upload_to ='uploads/photo/staffs/')
    pin = models.IntegerField(verbose_name='PIN')
    roles = models.IntegerField(verbose_name='roles')
    expenditure = models.FloatField(default=0, verbose_name='expenditure')
    reward_sent = models.FloatField(default=0, verbose_name='reward_sent')
    unclaimed_funds = models.FloatField(default=0, verbose_name='unclaimed_funds')
    status = models.IntegerField(default=1, verbose_name='status')
    ratings = models.CharField(max_length=255, verbose_name='ratings')
    facebook = models.CharField(max_length=255, verbose_name='facebook')
    instagram = models.CharField(max_length=255, verbose_name='instagram')
    twitter = models.CharField(max_length=255, verbose_name='twitter')
    youtube = models.CharField(max_length=255, verbose_name='youtube')
    tiktok = models.CharField(max_length=255, verbose_name='tiktok')
    snap = models.CharField(max_length=255, verbose_name='snap')
    message_board = models.CharField(max_length=255, verbose_name='message_board')
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')
    updated = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_updated')
    
    class Meta:
        db_table = "staffs"

class Brands(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    #birthday = models.DateField(verbose_name='DOB')
    gender = models.CharField(max_length=50, verbose_name='gender')
    email = models.EmailField(max_length=254, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='phone')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    password = models.CharField(max_length=255, verbose_name='password')
    state = models.CharField(max_length=255, verbose_name='state')
    country = models.CharField(max_length=255, verbose_name='country')
    company_name = models.CharField(max_length=255, verbose_name='company_name')
    company_email = models.EmailField(max_length=254, verbose_name='company_email')
    company_size = models.IntegerField(verbose_name='company_size')
    company_type = models.IntegerField(verbose_name='company_type')
    photo = models.ImageField(upload_to ='uploads/photo/brands/')
    pin = models.IntegerField(verbose_name='PIN')
    roles = models.IntegerField(verbose_name='roles')
    expenditure = models.FloatField(default=0, verbose_name='expenditure')
    reward_sent = models.FloatField(default=0, verbose_name='reward_sent')
    unclaimed_funds = models.FloatField(default=0, verbose_name='unclaimed_funds')
    status = models.IntegerField(default=1, verbose_name='status')
    ratings = models.CharField(max_length=255, verbose_name='ratings')
    facebook = models.CharField(max_length=255, verbose_name='facebook')
    instagram = models.CharField(max_length=255, verbose_name='instagram')
    twitter = models.CharField(max_length=255, verbose_name='twitter')
    youtube = models.CharField(max_length=255, verbose_name='youtube')
    tiktok = models.CharField(max_length=255, verbose_name='tiktok')
    snap = models.CharField(max_length=255, verbose_name='snap')
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')
    updated = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_updated')
    
    class Meta:
        db_table = "brands"

class Creators(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    birthday = models.DateField(verbose_name='DOB')
    gender = models.CharField(max_length=50, verbose_name='gender')
    email = models.EmailField(max_length=254, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='phone')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    password = models.CharField(max_length=255, verbose_name='password')
    state = models.CharField(max_length=255, verbose_name='state')
    country = models.CharField(max_length=255, verbose_name='country')
    content_category = models.CharField(max_length=255, verbose_name='content_category')
    content_type = models.CharField(max_length=255, verbose_name='content_type')
    levels = models.IntegerField(default=1, verbose_name='levels')
    photo = models.ImageField(upload_to ='uploads/photo/creators/')
    pin = models.IntegerField(verbose_name='PIN')
    roles = models.IntegerField(verbose_name='roles')
    earnings = models.FloatField(default=0, verbose_name='earnings')
    rewards = models.FloatField(default=0, verbose_name='rewards')
    bank_name = models.CharField(max_length=255, verbose_name='bank_name')
    account_num = models.CharField(max_length=255, verbose_name='account_num')
    status = models.IntegerField(default=1, verbose_name='status')
    ratings = models.CharField(max_length=255, verbose_name='ratings')
    facebook = models.CharField(max_length=255, verbose_name='facebook')
    instagram = models.CharField(max_length=255, verbose_name='instagram')
    twitter = models.CharField(max_length=255, verbose_name='twitter')
    youtube = models.CharField(max_length=255, verbose_name='youtube')
    tiktok = models.CharField(max_length=255, verbose_name='tiktok')
    snap = models.CharField(max_length=255, verbose_name='snap')
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created')
    updated = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_updated')
    
    class Meta:
        db_table = "creators"
