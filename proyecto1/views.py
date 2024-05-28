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

    # doc_externo = open("C:/Users/jorge/Desktop/proyecto1/proyecto1/template/template1.html")

    # plt = Template(doc_externo.read())
    
    # doc_externo.close()
    
    # doc_externo = get_template('template1.html')
    
    # documento = doc_externo.render({
    #     "nombre_persona": p1.nombre,
    #     "apellido_persona": p1.apellido,
    #     "fecha_actual": fecha_actual,
    #     "numeros": numeros  
    # })

    return render(request, "template1.html", {
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "fecha_actual": fecha_actual,
        "numeros": numeros  
    })