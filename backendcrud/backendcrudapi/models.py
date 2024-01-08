from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    acquired_on = models.DateField()
    customer_status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject