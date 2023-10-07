from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'first_name', 'last_name', 'contact_email', 'acquired_on',
                    'customer_status']
