# -*- encoding: utf-8 -*-
from django import forms
from models import Ciudad, Sexo, Tipo_empleado, Agrupacion, Escalafon, Seccion

class EmpleadoForm (forms.Form):
    apellido = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'form-control input-block-level', 'placeholder': 'Apellido'}, render_value=False)))
    nombre = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre'},render_value=False)))
    dni = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'DNI'},render_value=False)))
    domicilio = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Domicilio'},render_value=False)))
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Ciudad.objects.all())
    email = forms.CharField(widget=forms.EmailInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'em@il'},render_value=False)))
    sexo = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Sexo.objects.all())
    telefono = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nro. de telefono'},render_value=False)))
    tipo_empleado = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Tipo_empleado.objects.all())
    agrupacion = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Agrupacion.objects.all())
    escalafon = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Escalafon.objects.all())
    seccion = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Seccion.objects.all())

