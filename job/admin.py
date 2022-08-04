from django.contrib import admin
from .models import Category,Company,Vacancy,Workers

# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Workers)