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
from base.views import ProductTypeViewSet, DepartmentApiView, ProductApiView, VendorApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/types/",ProductTypeViewSet.as_view({'get':'list','post':'create'})),
    path("product/types/<int:pk>/", ProductTypeViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path("departments/",DepartmentApiView.as_view({'get':'list','post':'create'})),
    path("departments/<int:pk>/", DepartmentApiView.as_view({'get':'retrieve', 'patch' : 'partial_update', 'put':'update', 'delete':'destroy'})),
    path('product/', ProductApiView.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    path('vendor/', VendorApiView.as_view({'get': 'list', 'post': 'create'})),
    path('vendor/<int:pk>/', VendorApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

]   
