#configuracion del redireccionamiento 
from django.urls import path
from . import views
# crear el arreglo
urlpatterns=[
     path('',views.home,name='home'),
     path('listadoGeneros',views.listadoGeneros,name='listadoGeneros'),
     path('listadoDirectores',views.listadoDirectores,name='listadoDirectores'),
     path('listadoPaises',views.listadoPaises,name='listadoPaises'),
     path('listadoPeliculas',views.listadoPeliculas),
     #path para eliminar 
     path('eliminarGenero<id>',views.eliminarGenero,name='eliminarGenero'),
     path('eliminarDirector<id>',views.eliminarDirector,name='eliminarDirector'),
     path('eliminarPais<id>',views.eliminarPais,name='eliminarPais'),
     #path para nuevio genero
     path('nuevoGenero',views.nuevoGenero,name='nuevoGenero'),
     path('nuevoDirector',views.nuevoDirector,name='nuevoDirector'),
     path('nuevoPais',views.nuevoPais,name='nuevoPais'),
     #path para guardar el genero
     path('guardarGenero',views.guardarGenero,name='guardarGenero'),
     path('guardarDirector',views.guardarDirector,name='guardarDirector'),
     path('guardarPais',views.guardarPais,name='guardarPais'),
     #path para editar
     path('editarGenero<id>',views.editarGenero,name='editarGenero'),
     path('editarDirector<id>',views.editarDirector,name='editarDirector'),
     path('editarPais<id>',views.editarPais,name='editarPais'),
     #path para acualizar
     path('procesarActualizacionGenero',views.procesarActualizacionGenero,name='procesarActualizacionGenero'),
     path('procesarActualizarDirector',views.procesarActualizarDirector,name='procesarActualizarDirector'),
     path('procesarActualizarPais',views.procesarActualizarPais,name='procesarActualizarPais'),
     #path para cines
     path('gestionCines',views.gestionCines,name='gestionCines'),
     path('guardarCine',views.guardarCine,name='guardarCine'),
     path('listadoCines',views.listadoCines,name='listadoCines'),

     
     
     
     ]