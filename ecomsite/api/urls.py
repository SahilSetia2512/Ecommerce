from django.urls import path
from .import views
urlpatterns=[
    #API
    path('products/',views.ProductList.as_view()),
    path('products/<int:pk>',views.Delete.as_view()),
    path('orders/',views.Orders.as_view()),

    #API_AUTH
    path('signup/',views.signup),
    path('login/',views.login),
]