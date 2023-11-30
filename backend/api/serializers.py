from .models import *
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=['id','name']

class CategoryCountrySerializer(serializers.ModelSerializer):
    country=CountrySerializer(many=True)
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields=['id','country','name','photo_url']
        depth = 1

    def get_photo_url(self, category):
        request = self.context.get('request')
        photo_url = category.image.url
        return request.build_absolute_uri(photo_url)

class BrandCountrySerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model=Brand
        fields=['id','category','name','photo_url']

    def get_photo_url(self, brand):
        request = self.context.get('request')
        photo_url = brand.image.url
        return request.build_absolute_uri(photo_url)
    

class CouponSerializer(serializers.ModelSerializer):
    brand=BrandCountrySerializer()
    class Meta:
        model=Coupon
        fields=['id','description','brand','code']