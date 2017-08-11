# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from finanzas.apps.personal.forms import EmpleadoForm


def personal_create_view(request):
    form = EmpleadoForm()

    values = {
        'form':form
    }
    return render(request, 'formulario_empleado.html', values)

def personal_read_view(request):
    pass

def personal_update_view(request):
    pass

def personal_delete_view(request):
    pass
