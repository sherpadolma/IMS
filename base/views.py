from django.shortcuts import render
from .models import ProductType, Department, Product, Vendor, Sell, Purchase, Rating
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from .serializers import ProductTypeSerializer, DepartmentSerializer, ProductSerializer, VendorSerializer, UserSerializer,LoginSerializer, SellSerializer, PurchaseSerializer, RatingSerializer, GroupSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Sum, Avg


# Create your views here.
# def home(request):
#     return render(request, 'home.html')
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class DepartmentApiView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        queryset = self.get_queryset()  # It will get all the objects from the database
        serializer = self.get_serializer(
            queryset, many=True
        )  # It will serialize the queryset for JSON serialization object to JSON
        return Response(serializer.data)

    # Custom method to create a new department
    def create(self, request):
        serializer = self.get_serializer(
            data=request.data
        )  # it contain Json (request.data) # It will serialize the request data for JSON serialization object to JSON
        if serializer.is_valid(
            raise_exception=True
        ):  # It will validate the serializer data
            serializer.save()  # It will save the serializer data to the database
            return Response(
                serializer.data, status=201
            )  # It will return the serialized data and status code
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk):
        # try:
        #    query_set =  Department.objects.get(id=pk)
        # except:
        #     return Response({'error' : 'No matching data found!'}) # By default dictionary is converted onto json by Response class

        query_set = self.get_object()

        serializer = self.get_serializer(query_set, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        queryset = self.get_object()

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk):
        queryset = self.get_object()  # get_object is used to
        queryset.delete()
        return Response()

    def partial_update(self, request, pk):
        query_set = self.get_object()

        serializer = self.get_serializer(query_set, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupApiViwe(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserApiView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  #empty cuz no need of premission for this view..

    def register(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get("username")
            password = request.data.get("password")

            user = authenticate(username=username, password=password)
            if user == None:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED,)
            else:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

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
    
class SellApiView(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer 

class RatingApiView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer 
          
class ProductApiView(GenericViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     permission_classes = [DjangoModelPermissions]  
     

     def best_selling(self,request):
        queryset = (Product.objects.all().annotate(total_sell_quantity=Sum( "sell__quantity" )).order_by("-total_sell_quantity"))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
     
     def most_purchased(self,request):
         queryset = Product.objects.all().annotate(total_purchased_quantity=Sum('purchases__quantity')).order_by('-total_purchased_quantity') # adding field and value
         serializer = self.get_serializer(queryset, many=True)
         return Response(serializer.data)
     
     def top_rated(self,request):
         queryset = Product.objects.all().annotate(avg_rating=Avg('ratings__rating')).order_by('-avg_rating')
         serializer = self.get_serializer(queryset, many=True)
         return Response(serializer.data)
        
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
        
         

 
         
            