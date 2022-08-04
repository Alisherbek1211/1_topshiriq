from rest_framework import serializers 
from .models import Category,Company,Vacancy,Workers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'