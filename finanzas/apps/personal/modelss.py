# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ciudad(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.descripcion

class Persona(models.Model):
    apellido = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 11)
    email = models. EmailField()
    direccion = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = "Personas"

    def __unicode__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Jerarquia(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Jerarquias"

    def __unicode__(self):
        return self.descripcion

class Tipo_empleado(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de Empleados"

    def __unicode__(self):
        return self.descripcion

class Seccion(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Secciones"

    def __unicode__(self):
        return self.descripcion

class Agrupacion(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Agrupaciones"

    def __unicode__(self):
        return self.descripcion

class Escalafon(models.Model):
    descripcion = models.CharField(max_length = 30)
    agrupacion = models.ForeignKey(Agrupacion)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Escalafones"

    def __unicode__(self):
        return self.descripcion

class Sexo (models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Sexos"

    def __unicode__(self):
        return self.descripcion

class Empleado(models.Model):
    persona = models.ForeignKey(Persona)
    seccion = models.ForeignKey(Seccion)
    sexo = models.ForeignKey(Sexo)
    tipo_empleado = models.ForeignKey(Tipo_empleado)
    agrupacion = models.ForeignKey(Agrupacion)

    class Meta:
        #ordering = ['descripcion']
        verbose_name_plural = "Empleados"
