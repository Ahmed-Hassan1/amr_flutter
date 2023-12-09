from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(User_Number)
class UserAdmin(admin.ModelAdmin):
    list_display=["number","country","extension"]

    list_filter=["country"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields=['country']

    list_display=["name","countries"]
    list_filter=["country"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    autocomplete_fields=['country']

    list_display=["name","category","countries","topStore"]

    list_filter=["category","country"]

    list_editable=["topStore"]

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=["name","extension"]

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display=["description","brand"]
    list_filter=["brand"]