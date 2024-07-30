from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<int:id>/', views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('eliminarDirector/<int:id>/', views.eliminarDirector, name='eliminarDirector'),
    path('listadoPaises/', views.listadoPaises),
    path('listadoPeliculas/', views.listadoPeliculas),
    path('editarGenero/<int:id>/', views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/', views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('editarDirector/<int:id>/', views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector/', views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('gestionCines/', views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    path('listadoCines', views.listadoCines, name='listadoCines'),
    path('char/', views.chartview, name='chartview'),
]
