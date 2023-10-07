from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = productCategory()
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # code = serializers.CharField()
    # name = serializers.CharField()
    # desc = serializers.CharField(allow_blank=True, required=False)
    # images = serializers.CharField(allow_blank=True, required=False)
    # category = serializers.CharField(source='category.category')  # Use source to access the related category's category field

    class Meta:
        model = productList
        fields = '__all__'