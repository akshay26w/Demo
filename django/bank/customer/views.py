from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_django_customer_page(request):
    return HttpResponse("Welcome to Django Configurations...!")
