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






def personal_update_view(request):
    pass





def personal_delete_view(request, empleado_id):
    #empleado = Empleado.objects.get(id=empleado_id).delete()

    #lista = Empleado.objects.all()
    #values = {
    #   'lista': lista,
    #}
    #return render(request, 'lista_empleado.html', values)
    pass




def personal_cargartxt_view(request):

    return render(request, 'cargar_txt.html')
    return render(request, 'formulario_empleado.html')

    # mensaje = "Los datos no son validos :P"
        # values = {
        # 'form':form,
        # 'mensaje':mensaje
        #     }





    # datos2 = []
    # datos3 = []

    # file = open('liqpoli.txt', 'r')

    # contenido = file.readlines()

    # for i in range(0, len(contenido), 1):

    # dato1 = contenido[i].find('\t')
    # dato2 = contenido[i].find('\t', dato1 + 1)
    # dato3 = contenido[i].find('\t', dato2 + 1)


    # valor1 = float(contenido[i][0:dato1])
    # valor2 = float(contenido[i][dato1 + 1:dato2])
    # valor3 = float(contenido[i][dato2 + 1:dato3])

    return render(request, 'cargar_txt.html')





