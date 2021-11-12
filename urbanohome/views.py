from django.shortcuts import render

# Create your views here.

def index(request):
    myData = [
        {'title': 'Matera',
         'precio': 1000},
        {'title': 'Planta',
         'precio': 10000},
    ]
    
    return render(request, 'urbanohome/index.html', {
        'products': myData
    })