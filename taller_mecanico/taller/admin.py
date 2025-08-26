# taller/admin.py
from django.contrib import admin
from .models import Mecanico, Vehiculo, Procedimiento

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'especialidad')
    search_fields = ('nombre', 'especialidad')
    list_filter = ('especialidad',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'modelo', 'anio', 'dueño')
    search_fields = ('patente', 'modelo', 'dueño')
    list_filter = ('anio',)

@admin.register(Procedimiento)
class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vehiculo', 'mecanico', 'descripcion')
    search_fields = ('nombre', 'vehiculo__patente', 'mecanico__nombre')
    list_filter = ('mecanico',)
    autocomplete_fields = ['vehiculo', 'mecanico'] # Mejora la selección de FK