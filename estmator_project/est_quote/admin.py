from django.contrib import admin
from .models import Product, Quote, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Quote)
