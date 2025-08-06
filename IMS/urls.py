"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import ProductTypeViewSet, DepartmentApiView, ProductApiView, VendorApiView, UserApiView, SellApiView,PurchaseApiView, RatingApiView, GroupApiViwe

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/types/",ProductTypeViewSet.as_view({'get':'list','post':'create'})),
    path("product/types/<int:pk>/", ProductTypeViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path("departments/",DepartmentApiView.as_view({'get':'list','post':'create'})),
    path("departments/<int:pk>/", DepartmentApiView.as_view({'get':'retrieve', 'patch' : 'partial_update', 'put':'update', 'delete':'destroy'})),

    path("user/",UserApiView.as_view({'get':'list','post':'create'})),
    path('register/', UserApiView.as_view({'post': 'register'})),
    path('login/', UserApiView.as_view({'post': 'login'})),

    path('groups/', GroupApiViwe.as_view({'get': 'list'})),

    path('products/', ProductApiView.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:pk>/', ProductApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

    path('purchases/', PurchaseApiView.as_view({'get': 'list', 'post': 'create'})),
    path('purchases/<int:pk>/', PurchaseApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    
    path('most/purchased/products/', ProductApiView.as_view({'get':'most_purchased'})),

    path('top/rated/products/', ProductApiView.as_view({'get':'top_rated'})),

    path('product/ratings/', RatingApiView.as_view({'get': 'list', 'post': 'create'})),
    path('product/ratings/<int:pk>/', RatingApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
   
    path('vendors/', VendorApiView.as_view({'get': 'list', 'post': 'create'})),
    path('vendors/<int:pk>/', VendorApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    
    path("sells/",SellApiView.as_view({'get':'list','post':'create'})),
    path("sells/types/<int:pk>/", SellApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('best/selling/product/', ProductApiView.as_view({'get': 'best_selling'})),

]   
