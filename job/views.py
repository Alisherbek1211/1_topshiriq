from django.shortcuts import render
from rest_framework import generics,views
from serializers import CategorySerializer,VacancySerializer,WorkersSerializer,CompanySerializer
from models import Category,Vacancy,Workers,Company
from rest_framework.permissions import IsAuthenticated


class CategoryListView(views.APIView):
    serializer_class = CategorySerializer
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        workers = Workers.objects.all()

        queryset = Category.objects.aggregate(
            # workers_count=models.Count('workers'),

        )
        return queryset

class ListView(generics.ListAPIView):
    # serializer_class = 