from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {
        'cars': cars
    })

cars = [
    {'make': 'Jeep', 'model': 'Grand Cherokee', 'year': 2018, 'kind': 'SUV'},
    {'make': 'Porsche', 'model': 'Boxster', 'year': 2015, 'kind': 'sportscar'},
]