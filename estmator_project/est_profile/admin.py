from django.contrib import admin
from .models import Client, Company, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Client)
