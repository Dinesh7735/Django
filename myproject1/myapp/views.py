from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('This is my first project')

def about(request):
    return HttpResponse('This is about section')