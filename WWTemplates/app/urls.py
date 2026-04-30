from django.urls import path
from app.views import *

urlpatterns = [
    path('home/',home, name='home'),
]