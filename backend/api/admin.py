from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Coupon)
admin.site.register(User_Number)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields=['country']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    autocomplete_fields=['country']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields=['name']