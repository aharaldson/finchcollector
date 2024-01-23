from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_service/', views.add_service, name='add_service'),
  path('cars/<int:car_id>/assoc_mod/<int:mod_id>/', views.assoc_mod, name='assoc_mod'),
  path('cars/<int:car_id>/unassoc_mod/<int:mod_id>/', views.unassoc_mod, name='unassoc_mod'),
  path('cars/mods/', views.ModList.as_view(), name='mods_index'),
  path('cars/mods/<int:pk>/', views.ModDetail.as_view(), name='mods_detail'),
  path('cars/mods/create/', views.ModCreate.as_view(), name='mods_create'),
  path('cars/mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mods_update'),
  path('cars/mods/<int:pk>/delete/', views.ModDelete.as_view(), name='mods_delete'),
]
