from django.contrib import admin
from .models import (
    Product, Quote, Category, QuoteModifiers, QuoteOptions, ProductProperties
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(QuoteModifiers)
admin.site.register(QuoteOptions)
admin.site.register(ProductProperties)
