from rest_framework import serializers,permissions
from shop.models import Products,Order
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Products
        fields=['id','title','price','discount_price','category','description','image']

class OrderSerializer(serializers.ModelSerializer):
    items=serializers.ReadOnlyField()
    total=serializers.ReadOnlyField()
    user=User
    class Meta:
        model=Order
        fields=['id','items','name','address','city','state','zipcode','total','user']




