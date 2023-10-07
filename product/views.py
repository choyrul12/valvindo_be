from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import F

class product_list(APIView):
    def get(self, request):
        objCategory = productCategory.objects.all()
        category = CategorySerializer(objCategory, many=True)
        objProduct = productList.objects.all()
        product = ProductSerializer(objProduct, many=True)

        result = []
        for item in category.data:
            list_product = {
                "id": item["id"],
                "category": item["category"],
                "products": []
            }

            for detail in product.data:
                if detail["category"] == item["id"]:
                    list_product["products"].append({
                        "id": detail["id"],
                        "name": detail["name"],
                        "images": detail["images"],
                    })

            result.append(list_product)
        return Response(result)
