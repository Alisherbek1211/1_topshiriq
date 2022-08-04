from django.db import models


class Category(models.Model):
    neme = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Company = models.ForeignKey(Company,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    sales_from = models.IntegerField()
    sales_to = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.count


class Workers(models.Model):
    first_name = models.CharField(max_length=255)
    sales_from = models.IntegerField()
    sales_to = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
