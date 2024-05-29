from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



def saludo(request):

    p1 = Persona("Juan", "Gomez")
    
    numeros = ["uno", "dos", "tres", "cuatro", "cinco"]
    

    fecha_actual= datetime.datetime.now()

   
    return render(request, "template1.html", {
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "fecha_actual": fecha_actual,
        "numeros": numeros  
    })
    
def contenido(request):
    
    fecha_actual= datetime.datetime.now()
    
    return render(request, "contenido.html", {
         "fecha_actual": fecha_actual  
    })
    
def contenido2(request):
    
  
    
    return render(request, "contenido2.html")