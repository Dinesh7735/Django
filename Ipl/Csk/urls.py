from django.urls import path
from Csk.views import *

urlpatterns = [
    path('Csk/',Csk,name='Csk'),
]