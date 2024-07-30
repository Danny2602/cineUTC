from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Genero,Director,Pais,Pelicula,Cine
#controlar los mensajes 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
#renderizando el template Listado generos
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html",
                  {'generos':generosBdd}
                  )
#se recibe el id para eliminar un genero 
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,'Genero Eliminado')
    return redirect('listadoGeneros')
#se ingresa un nuevo genero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')
#insertando nuevos generos 
def guardarGenero(request):
    nom=request.POST['nombre']
    des=request.POST['descripcion']
    fot=request.FILES.get('foto')
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot)
    messages.success(request,'Genero registrado exitosamente')
    return redirect('listadoGeneros')
#renderizando actualizacion de datos 
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})
#actualizamos los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsulta=Genero.objects.get(id=id)
    generoConsulta.nombre=nombre
    generoConsulta.descripcion=descripcion
    generoConsulta.save()
    messages.success(request,'Genero actualizo exitosamente')
    return redirect('listadoGeneros')


#Seccion de Directores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,"listadoDirectores.html",
                  {'directores':directoresBdd}
                  )
#nuevo director 
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')
#guardar director
def guardarDirector(request):
    dni1=request.POST['dni']
    ape=request.POST['apellido']
    nom=request.POST['nombre']
    es = 'estado' in request.POST and request.POST['estado'] == 'on'
    fot=request.FILES.get('fotografia')
    nuevoDirector=Director.objects.create(dni=dni1,apellido=ape,nombre=nom,estado=es,fotografia=fot)
    messages.success(request,'Director registrado exitosamente')
    return redirect('listadoDirectores')
#eliminar Director
def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,'Director Eliminado')
    return redirect('listadoDirectores')
#actualizar director
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html',{'directorEditar':directorEditar})
#actualizar los nuevos datos en bdd director
def procesarActualizarDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    ape=request.POST['apellido']
    nom=request.POST['nombre']
    fot=request.FILES.get('fotografia')
    es = 'estado' in request.POST and request.POST['estado'] == 'on'
    directorConsulata=Director.objects.get(id=id)
    directorConsulata.dni=dni
    directorConsulata.apellido=ape
    directorConsulata.nombre=nom
    directorConsulata.estado=es
    directorConsulata.fotografia=fot
    directorConsulata.save()
    messages.success(request,'Director actualizado')
    return redirect('listadoDirectores')
#Seccion Paises 
def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render (request,"listadoPaises.html",
                   {'paises':paisesBdd}
                   )
#nuevo pais
def nuevoPais(request):
    return render(request,'nuevoPais.html')
#agregar pais
def guardarPais(request):
    nom=request.POST['nombre']
    con=request.POST['continente']
    cap=request.POST['capital']
    paisGuardar=Pais.objects.create(nombre=nom,continente=con,capital=cap)
    messages.success(request,'nuevo Pais creado Exitosamente')
    return redirect('listadoPaises')
#eliminar pais
def eliminarPais(request,id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request,'Pais Eliminado')
    return redirect('listadoPaises')
#editar pais
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html',{'paisEditar':paisEditar})
#actualizar pais
def procesarActualizarPais(request):
    id=request.POST['id']
    nom=request.POST['nombre']
    con=request.POST['continente']
    cap=request.POST['capital']
    paisConsulta=Pais.objects.get(id=id)
    paisConsulta.nombre=nom
    paisConsulta.continente=con
    paisConsulta.capital=cap
    paisConsulta.save()
    messages.success(request,'Pais actualizado')
    return redirect('listadoPaises')

#seccion Peliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render (request,"listadoPeliculas.html",
                    {'pelicula':peliculasBdd}
                )

#funcion para gestionar el creud de cine
def gestionCines(request):
    return render(request,'gestionCines.html')

def guardarCine(request):
    nom=request.POST["nombre"]
    dic=request.POST["direccion"]
    telf=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dic,telefono=telf)
    return JsonResponse({
        'estado': True,
        'mensaje':'Nuevos cine registrado'
        
    })
def listadoCines(request):
    cinesBdd=Cine.objects.all();
    return render(request,"listadoCines.html",{'cines':cinesBdd})

#def exportCines(request):
    # dataCines = Cine.objects.all()
    #breturn render(request,"exportCines.html", {'cines': dataCines})
#def exportCinesPDF(request):
    #llamar a todos los datos del modelo cina
    #cines = Cine.objects.all()
    #llamar al template con el render string
    #html_string = render_to_string('exportCines.html', {'cines': cines})
    #almacenar como un archivo html
    #html = HTML(string=html_string)
    #leer todo el html guardado y convvertirlo en un pdf
    #pdf = html.write_pdf()
    #dar una respuesta como pdf(archivo)
    #response = HttpResponse(pdf, content_type='application/pdf')
    #nombrar y dar una extension al archivo expotado
    #response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
    #exportar archivo
    #return response
    