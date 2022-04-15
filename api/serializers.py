from rest_framework import serializers
from .models import Admin,city,major

class AdminSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Admin
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):    
    class  Meta:
        model = city
        fields = '__all__'


class majorSerializer(serializers.ModelSerializer):
    class  Meta:
        model = major
        fields = '__all__'

