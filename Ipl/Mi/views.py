from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Mi(request):
    return HttpResponse('<h1> Hitman </h1>')