# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import Context, Template, RequestContext

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from .forms import LoginForm, ChangePassForm

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('principal'))
    form = LoginForm()#declaramos una variable que reciba los campos del formulario
    mensaje = '' #decaromos una variable con un mensaje vacio
    if request.method == 'POST':#validamos que los datos vengan por Post
        form = LoginForm(request.POST)#le pasamos el request a loginForm
        if form.is_valid(): #verificamos que el formato de los datos sea correcto
            usuario = form.data['user']#asignamos a los datos de usuario a una variable usuario
            password = form.data['password']#asignamos a los datos de password a una variable password
            user = authenticate(username = usuario, password = password)#validamos que el usuario y la contraseña sean correctos
            if user is not None and user.is_active:#SI usuario y contraseña son correctos
                login(request, user)
                return HttpResponseRedirect('principal')
            else:
                form = LoginForm()#renderizamos loguin.html con un mensaje de error
                mensaje = 'Usuario y/o password incorrecto, verifíquelo e inténtelo nuevamente.'
        else:
            form = LoginForm()#renderizamos loguin.html con un mensaje de error
            mensaje = 'Debe completar ambos campos.'
    values = {
        'form' : form,
        'mensaje' : mensaje,
    }

    return render(request, 'login.html', values)

@login_required
def principal_view(request):

    return render(request, 'principal.html')

@login_required
def change_pass_view(request):
    form = ChangePassForm()
    mensaje = ""
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            username = request.user
            password = form.data['password_actual']
            user = authenticate(username=username, password=password)
            if user is not None:
                password_nuevo = form.cleaned_data['password_nuevo']
                password_confirmar = form.cleaned_data['password_confirmar']
                if password_nuevo == password_confirmar:
                    user.set_password(password_nuevo)
                    try:
                        user.save()
                    except Exception, e:
                        raise e
                    mensaje = "Password modificada exitosamente."
                else:
                    mensaje = "Los password no coinciden."
            else:
                mensaje = "Password actual no coincide con el usuario logueado."
        else:
            mensaje = "Debe completar todos los campos."

        values = {
            'mensaje':mensaje,
            'form':form
            }
        return render(request, 'change_pass.html', values)

    values = {
        'mensaje':mensaje,
        'form':form
    }
    return render(request, 'change_pass.html', values)





@login_required
def logout_view(request):
    logout(request) #cierra sesion
    return redirect(reverse('login'))#redirecciona a login



def reset_pass_view(requet):
    pass
