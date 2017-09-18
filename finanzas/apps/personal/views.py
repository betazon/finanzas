# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from finanzas.apps.personal.forms import EmpleadoForm
from .models import *

def personal_create_view(request):
    form = EmpleadoForm()

    mensaje= ""
    if request.method == 'POST':

        form = EmpleadoForm(request.POST)

        if form.is_valid():
            personales = Persona()
            empleado = Empleado()

            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            documento = form.cleaned_data['dni']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data ['email']
            direccion = form.cleaned_data['domicilio']
            ciudad = form.cleaned_data['ciudad']
            agrupacion = form.cleaned_data['agrupacion']
            seccion = form.cleaned_data['seccion']
            sexo = form.cleaned_data['sexo']
            tipo_empleado = form.cleaned_data['tipo_empleado']

            personales.apellido = apellido
            personales.nombre = nombre
            personales.documento = documento
            personales.telefono = telefono
            personales.email = email
            personales.direccion = direccion
            personales.ciudad_id = ciudad.id
            personales.save()

            empleado.agrupacion_id = agrupacion.id
            empleado.persona = personales
            empleado.seccion = seccion
            empleado.sexo = sexo
            empleado.tipo_empleado = tipo_empleado

            empleado.save()

        else:
            mensaje = "Los datos no son validos :P"
    values = {
        'form':form,
        'mensaje':mensaje
             }
    return render(request, 'formulario_empleado.html', values)








def personal_list_view(request):
    lista = Empleado.objects.all()

    values = {
        'lista':lista,
    }
    return render(request, 'lista_empleado.html', values)






def personal_update_view(request,idempleado):

     idempleado = request.POST.get('idempleado')







def personal_delete_view(request, empleado_id):
    pass




def personal_cargartxt_view(request):

    infile = open('liqpoli.txt', 'r')
    print('>>> Lectura del fichero línea a línea')
    for line in infile:
        print(line)
    infile.close()

    return render(request, 'cargar_txt.html')





