from django.shortcuts import render
from .models import ProductType, Department, Product, Vendor
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from .serializers import ProductTypeSerializer, DepartmentSerializer, ProductSerializer, VendorSerializer
from rest_framework import status

# Create your views here.
# def home(request):
#     return render(request, 'home.html')
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class DepartmentApiView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self,request):
        queryset = self.get_queryset()
        Serializer = self.get_serializer(queryset,many=True)
        return Response(Serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request,pk):
        # try:
        #     queryset = Department.objects.get(id=pk)
        # except:
        #     return Response({"error": "No mactching data found"})

        queryset = self.get_object()
        
        serializer = self.get_serializer(queryset, data=request.data) #By default dictonary is converted into json by response class
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        queryset = self.get_object()
        
        serializer = self.get_serializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
    def retrieve(self, request, pk):
        queryset = self.get_object()

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        queryset = self.get_object()

        queryset.delete()
        return Response()
    
class ProductApiView(GenericViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     def list(self,request):
        queryset = self.get_queryset()
        Serializer = self.get_serializer(queryset,many=True)
        return Response(Serializer.data)
     
     def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
     def update(self,request,pk):
        #  try:
        #      product = Product.objects.get(id=pk)
        #  except Product.DoesNotExist:
        #      return Response({"error": "Product not found"})
         
        queryset = self.get_object()
        
        serializer = self.get_serializer(queryset, data=request.data) #By default dictonary is converted into json by response class
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
     def partial_update(self, request, pk):
        queryset = self.get_object()
        
        serializer = self.get_serializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
     def retrieve(self, request, pk):
        queryset = self.get_object()

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
     def destroy(self, request, pk):
        queryset = self.get_object()

        queryset.delete()
        return Response()
     
class VendorApiView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer     
        
         

 
         
            