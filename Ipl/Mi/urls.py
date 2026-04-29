from django.urls import path
from Mi.views import *

urlpatterns = [
    path('Mi/', Mi, name= 'Mi'),
]