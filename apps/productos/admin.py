from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
