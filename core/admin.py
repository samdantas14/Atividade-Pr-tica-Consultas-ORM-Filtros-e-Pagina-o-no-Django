from django.contrib import admin

from .models import Autor, Categoria, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "ano_publicacao")
    list_filter = ("autor", "categoria")
    search_fields = ("titulo", "autor__nome")