# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Context, Template, RequestContext

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import LoginForm


def login_view(request):
    form = LoginForm()#declaramos una variable que reciba los campos del formulario
    mensaje = '' #decaromos una variable con un mensaje vacio
    if request.method == 'POST':#validamos que los datos vengan por Post
        form = LoginForm(request.POST)#le pasamos el request a loginForm
        if form.is_valid(): #verificamos que el formato de los datos sea correcto
            usuario = form.data['user']#asignamos a los datos de usuario a una variable usuario
            password = form.data['password']#asignamos a los datos de password a una variable password
            user = auth.authenticate(username = usuario, password = password)#validamos que el usuario y la contraseña sean correctos
            if user is not None and user.is_active:#SI usuario y contraseña son correctos
                request.session['usuario'] = usuario
                request.session['password'] = password
                print(user)
                print(usuario)
                values = {
                    'user':user,
                }
                return render(request, 'profile.html', values)#redireccionamos a profile.html
            else:
                login = LoginForm()#renderizamos loguin.html con un mensaje de error
                mensaje = 'Usuario y/o password incorrecto, verifiquelo y try again'

    values = {
        'form':form,
        'mensaje': mensaje,
    }

    return render(request, 'login.html', values)

def profile_view(request):

    values={'user':user}
    return render(request, 'profile.html', values)




def change_pass_view(request):
    pass

def reset_pass_view(request):
    pass

def logout_view(request):
    pass
