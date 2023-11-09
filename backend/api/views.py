from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
# Create your views here.

def api_home(request):
    countries=Country.objects.all()
    countries_serial=CountrySerializer(countries,many=True)

    categories=Category.objects.all()
    categories_serial=CategoryCountrySerializer(categories,many=True,context={"request":request})

    brands=Brand.objects.all()
    brands_serial=BrandCountrySerializer(brands,many=True)

    coupons=Coupon.objects.all()
    coupons_serial=CouponSerializer(coupons,many=True)

    return JsonResponse([countries_serial.data,categories_serial.data,brands_serial.data,coupons_serial.data],safe=False)