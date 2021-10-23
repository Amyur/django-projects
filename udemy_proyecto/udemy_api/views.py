from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from udemy_api.models import Paises
from udemy_api.serializers import PaisesSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET", "POST"])
def paises_list(request):
    if request.method == "GET":
        paises = Paises.objects.all()

        name = request.GET.get("name", None)
        if name is not None:
            paises = paises.filter(name__icontains=name)

        paises_serializer = PaisesSerializer(paises, many=True)
        return(JsonResponse(paises_serializer.data, safe=False))

    elif request.method == "POST":
        paises_data = JSONParser().parse(request)
        paises_serializer = PaisesSerializer(data=paises_data)
        if paises_serializer.is_valid():
            paises_serializer.save()
            return JsonResponse(paises_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(paises_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def paises_detail(request, pk): #pk es el id, primary key
    try:
        paises = Paises.objects.get(pk=pk)
    except Paises.DoesNotExist:
        return(JsonResponse({"messaje": "The country does not exist"}))
    
    if request.method == "GET":
        paises_serializer = PaisesSerializer(paises)
        return(JsonResponse(paises_serializer.data))
    
    elif request.method == "PUT":
        paises_data = JSONParser().parse(request)
        paises_serializer = PaisesSerializer(paises, data=paises_data)
        if paises_serializer.is_valid():
            paises_serializer.save()
            return(JsonResponse(paises_serializer.data))
        return(JsonResponse(paises_serializer.errors, status=status.HTTP_400_BAD_REQUEST))

    elif request.method == "DELETE":
        paises.delete()
        return(JsonResponse({"message":"Country was deleted sucesfuly"}, status=status.HTTP_205_RESET_CONTENT))
