import json
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

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


def api_cats(request):
    cats=Category.objects.all()
    country=Country.objects.get(name="Egypt")
    cats2=Category.objects.filter(country__name="Egypt")
    categories_serial=CategoryCountrySerializer(cats2,many=True,context={"request":request})
    print(categories_serial.data)
    
    return JsonResponse(categories_serial.data,safe=False)

@csrf_exempt
def api_create_user(request):
    print(request.body)
    user_info=json.loads(request.body)
    print(user_info)

    country=Country.objects.get(name=user_info['country'])
    User_Number.objects.get_or_create(number=user_info['number'],country=country)
    cats2=Category.objects.filter(country__name=user_info['country'])
    categories_serial=CategoryCountrySerializer(cats2,many=True,context={"request":request})
    print(categories_serial.data)
    return JsonResponse(categories_serial.data,safe=False)