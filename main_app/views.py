from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Mod
from .forms import ServiceForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.mods.all().values_list('id')
    mods_car_doesnt_have = Mod.objects.exclude(id__in=id_list)
    service_form = ServiceForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'service_form': service_form, 'mods': mods_car_doesnt_have
     })

def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'kind']

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'kind']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'

class ModList(ListView):
  model = Mod
  template_name = 'cars/mod_list.html'

class ModDetail(DetailView):
  model = Mod
  template_name = 'cars/mod_detail.html'

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'
  template_name = 'cars/mod_form.html'

class ModUpdate(UpdateView):
    model = Mod
    fields = ['name']
    template_name = 'cars/mod_update_form.html'

class ModDelete(DeleteView):
  model = Mod
  template_name = 'cars/mod_confirm_delete.html'
  success_url = '/mods'

def assoc_mod(request, car_id, mod_id):
    car_instance = Car.objects.get(id=car_id)
    mod_instance = Mod.objects.get(id=mod_id)
    car_instance.mods.add(mod_instance)
    return redirect('detail', car_id=car_id)

def unassoc_mod(request, car_id, mod_id):
    car_instance = Car.objects.get(id=car_id)
    mod_instance = Mod.objects.get(id=mod_id)
    car_instance.mods.remove(mod_instance)
    return redirect('detail', car_id=car_id)