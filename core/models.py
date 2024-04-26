from django.db import models
import random
import string
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='core/logo/')
    file = models.FileField(upload_to='core/files/')
    company_code = models.CharField(max_length=4)
    def __str__(self):
        return  str(f"{self.id}-{self.name}")

class Client(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    agency_name = models.CharField(max_length=200)
    GST_number = models.CharField(max_length=200)
    GST_file = models.FileField(upload_to='core/files/')
    Aadhar = models.CharField(max_length=200)
    Aadhar_file = models.FileField(upload_to='core/files/')
    PAN_number = models.CharField(max_length=200)
    PAN_file = models.FileField(upload_to='core/files/')
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200,blank=True,null=True)
    company = models.ForeignKey(Company,null=True,blank=True,on_delete=models.CASCADE)
    vendor_code = models.CharField(max_length=19,unique=True,null=True,blank=True)
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.company and not self.vendor_code:
            # Generate a random 15-digit number string
            random_str = ''.join(random.choices(string.digits, k=15))
            # Combine company code and random string
            self.vendor_code = f"{self.company.company_code}{random_str}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name 


class BankAccount(models.Model):
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    def __str__(self):
        return self.account_holder_name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name