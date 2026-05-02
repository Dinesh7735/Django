from django.shortcuts import render

# Create your views here.

def index(request):
    studs = [{'name' : 'Dinesh', 'age' : 24}, {'name' : 'Shivam', 'age' : 17}, {'name' : 'Santosh', 'age' : 26}]

    return render(request, 'index.html', context = {'studs' : studs})