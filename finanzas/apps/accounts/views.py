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
    form = LoginForm()#declaramos una variable que reciba los campos del formulario
    mensaje = '' #decaromos una variable con un mensaje vacio
    if request.method == 'POST':#validamos que los datos vengan por Post
        form = LoginForm(request.POST)#le pasamos el request a loginForm
        if form.is_valid(): #verificamos que el formato de los datos sea correcto
            usuario = form.data['user']#asignamos a los datos de usuario a una variable usuario
            password = form.data['password']#asignamos a los datos de password a una variable password
            user = authenticate(username = usuario, password = password)#validamos que el usuario y la contraseña sean correctos
            if user is not None and user.is_active:#SI usuario y contraseña son correctos
                #request.session['usuario'] = usuario
                #request.session['password'] = password
                #values = {
                #    'user':user,
                #}
                #return render(request, 'principal.html', values)#redireccionamos a profile.html
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
    mensaje = ""
    form = ChangePassForm()
    values = {
        'form':form,
        'mensaje':mensaje,
    }
    return render(request, 'change_pass.html', values)

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))



def reset_pass_view(requet):
    pass
