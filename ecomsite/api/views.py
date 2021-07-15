from rest_framework import generics,permissions
from .serializers import ProductSerializer,OrderSerializer
from shop.models import Products,Order
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse 
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout, authenticate
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data=JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token=Token.objects.create(user=user)
            return JsonResponse({"token":str(token)},status=201)
        except IntegrityError:
            return JsonResponse({"error":"That username has already been taken. Please choose a new username"},status=401)

def login(request):
    if request.method == 'POST':

        data=JSONParser().parse(request)
        user = user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({"error":"Check your username and password"},status=401)
        else :
            try:
                token =Token.objects.get(user=user)
            except:
                token=Token.objects.create(user=user)
            return JsonResponse({"token":str(token)},status=200)

class ProductList(generics.ListCreateAPIView):
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user

        return Products.objects.filter(user=user)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class Delete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Products.objects.filter(user=user)

class Orders(generics.ListCreateAPIView):
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)

# Create your views here.
