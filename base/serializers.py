from rest_framework import serializers
from .models import ProductType, Department, Product, Vendor, Sell, Purchase, Rating
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','groups','email', 'first_name','last_name']

    def create(self,validated_data):
        raw_password =  validated_data.pop('password') # remove and assigned password key and value which user sent and validated
        hash_password = make_password(raw_password) # hasing user's password using make_password function
        validated_data['password'] = hash_password  # Assigning hashed password as a validated data
        return super().create(validated_data)  # Passing the validated data to the parent class's create method to save the user instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


