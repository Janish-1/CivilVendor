from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(BankAccount)
admin.site.register(Contact)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.get_fields() if field.name not in ['id', 'address','GST_file','Aadhar_file','PAN_file']]
    list_editable = ['status']