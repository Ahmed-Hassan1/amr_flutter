from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Brand)
admin.site.register(Coupon)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields=['country']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields=['name']