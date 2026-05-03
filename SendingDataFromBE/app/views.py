from django.shortcuts import render

# Create your views here.
def index(request):
    d = {'name' : 'Dinesh', 'age' : 24}

    return render(request, 'index.html', d)