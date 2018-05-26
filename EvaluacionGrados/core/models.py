# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.

class Programa(models.Model):
    id_del_programa = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_del_programa = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.nombre_del_programa.encode("utf-8")


class User(AbstractUser):
    codigo_docente = models.CharField(max_length=10,  null=False)
    cedula = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    programa = models.ForeignKey(Programa, null=True, on_delete=models.CASCADE)   
    
    def __str__(self):
        return (self.first_name+' '+self.last_name).encode("utf-8")

class Estudiante(models.Model):
    codigo_del_estudiante = models.CharField(max_length=10, primary_key=True, null=False)
    cedula_del_estudiante = models.CharField(max_length=10, unique=True, null=False)
    identificacion = models.CharField(max_length=20, null=False, unique=True)
    nombres_del_estudiante = models.CharField(max_length=50, null=False)
    apellidos_del_estudiante = models.CharField(max_length=50, null=False)
    correo = models.EmailField(null=False, unique=True)
    fecha_nacimiento = models.DateField(null=True,  blank=True)
    fecha_sustentacion = models.DateField(null=True,  blank=True)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)
    

    def __str__(self):
        return (self.nombres+' '+self.apellidos).encode("utf-8")


class OpcionDeGrado(models.Model):
    id_opcion_grado = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_opcion_de_grado = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.nombre_opcion_de_grado.encode("utf-8")



class TrabajoGrado(models.Model):
    #id_trabajo_grado = models.CharField(max_length=10, primary_key=True, null=False)
    estudiante_1 = models.ForeignKey(Estudiante, related_name="%(class)s_estudiante1", on_delete=models.CASCADE)
    estudiante_2 = models.ForeignKey(Estudiante, null=True, blank=True, related_name="%(class)s_estudiante2", on_delete=models.CASCADE)
    opcion_de_grado = models.ForeignKey(OpcionDeGrado, null=False, on_delete=models.CASCADE)
    nombre_trabajo_de_grado = models.CharField(max_length=50, null=False, unique=True)
    programa = models.ForeignKey(Programa, null=False, on_delete=models.CASCADE)
    director = models.ForeignKey(User, null=False, related_name="%(class)s_director", on_delete=models.CASCADE)
    codirector = models.ForeignKey(User, null=True, blank=True, related_name="%(class)s_codirector", on_delete=models.CASCADE)
    jurado_1 = models.ForeignKey(User, null=False, related_name="%(class)s_jurado1", on_delete=models.CASCADE)
    jurado_2 = models.ForeignKey(User, null=True, blank=True, related_name="%(class)s_jurado2", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_trabajo_de_grado.encode("utf-8")

class CalificacionProyecto(models.Model):
    id_calificacion_proyecto = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_de_calificacion_proyecto = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_de_calificacion_proyecto.encode("utf-8")

class EvaluacionProyecto(models.Model):
    #id_evaluacion_proyecto = models.CharField(max_length=10, primary_key=True, null=False)
    trabajo_grado = models.ForeignKey(TrabajoGrado,  null=False, on_delete=models.CASCADE)
    activo_para_evaluar = models.BooleanField()
    titulo = models.BooleanField()
    descripcion_del_problema = models.BooleanField()
    hipotesis = models.BooleanField()
    objetivos_generales = models.BooleanField()
    objetivos_especificos = models.BooleanField()
    justificacion = models.BooleanField()
    marco_de_referencia_teorico_y_conceptual = models.BooleanField()
    metodologia = models.BooleanField()
    resultados_esperados = models.BooleanField()
    cronograma_de_actividades = models.BooleanField()
    recursos_o_presupuesto = models.BooleanField()
    literatura_citada = models.BooleanField()
    redaccion_y_ortografia = models.BooleanField()
    pertinencia_con_el_area_de_formacion_del_estudiante = models.BooleanField()
    recomendaciones_observaciones_correciones = models.TextField( null=True, blank=True)
    resultado_consolidado = models.ForeignKey(CalificacionProyecto,  null=True, blank=True, related_name="%(class)s_resultado_consolidado", on_delete=models.CASCADE)


    def __str__(self):
        return "Evaluacion del proyecto: "+str(self.trabajo_grado).encode("utf-8")