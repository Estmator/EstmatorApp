from django.contrib import admin
from .models import (
    Product, Quote, Category, QuoteModifiers, QuoteOptions,
    QuoteProperties, ProductProperties
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(QuoteModifiers)
admin.site.register(QuoteOptions)
admin.site.register(QuoteProperties)
admin.site.register(ProductProperties)
