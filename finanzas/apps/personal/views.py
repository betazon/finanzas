# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from finanzas.apps.personal.forms import EmpleadoForm

def personal_create_view(request):
    form = EmpleadoForm()
    mensaje= ""
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():

            form.save

        else:
            mensaje = "falta campos"




    values = {
        'form':form,
        'mensaje':mensaje
    }


    return render(request, 'formulario_empleado.html', values)
def personal_list_view(request):
    pass
def personal_update_view(request):
    pass
def personal_delete_view(request):
    pass
