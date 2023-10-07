from django.db import models

# Create your models here.
# models.py in your Django app
from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    acquired_on = models.DateField()
    customer_status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.company_name
