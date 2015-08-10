from django.contrib import admin
from .models import (
    Product, Quote, Category, ProductInQuote, LocVars, GlobalVars,
    GlobalMods
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(ProductInQuote)
admin.site.register(LocVars)
admin.site.register(GlobalVars)
admin.site.register(GlobalMods)
