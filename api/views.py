from functools import partial
from ntpath import join
from pydoc import doc
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Admin, city, major
from .serializers import AdminSerializer, CitySerializer,majorSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time import time

class admin_api(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class city_api(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = CitySerializer
    

class major_api(viewsets.ModelViewSet):
    queryset = major.objects.all()
    serializer_class = majorSerializer

    