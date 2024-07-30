from django.db import models

# Create your models here.
# Creando un modelo Genero: Terror, Accion ......
class Genero(models.Model):
    # autoincrementable autofield
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    #añadir un valor por defecto
    descripcion=models.CharField(max_length=50,default='')
    foto=models.FileField(upload_to='generos',null=True,blank=True)
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)

class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    apellido=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    fotografia=models.FileField(upload_to='director',null=True,blank=True)
    def __str__(self):
        fila="{0}: {1} {2}"
        return fila.format(self.id,self.nombre,self.apellido)

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    continente=models.CharField(max_length=20)
    capital=models.CharField(max_length=30)
    def __str__(self):
        fila="{0}: {1} {2}"
        return fila.format(self.id,self.nombre,self.continente)

class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsis=models.TextField()
    
    #clave foraneo de Genero
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    #clave foraneo de Director
    director=models.ForeignKey(Director,on_delete=models.CASCADE)
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.titulo)
    
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=250)
    direccion=models.CharField(max_length=250)
    telefono=models.CharField(max_length=10)
    
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.nombre,self.direccion)


