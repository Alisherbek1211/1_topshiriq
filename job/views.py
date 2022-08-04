from django.shortcuts import render
from rest_framework import generics,views
from .serializers import CategorySerializer,VacancySerializer,WorkersSerializer,CompanySerializer
from .models import Category,Vacancy,Workers,Company
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.db.models import Count,When

class CategoryListView(views.APIView):
    serializer_class = CategorySerializer
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        worker_count = Workers.objects.all().count()
        company_count = Company.objects.all().count()
        vacancy_count = Vacancy.objects.all().count()
        content = {
            'worker_count',worker_count,
            'company_count',company_count,
            'vacancy_count',vacancy_count,
        }
        return Response(content)
