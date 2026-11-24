
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Autor, Categoria, Livro


def lista_livros(request):

    pesquisa = request.GET.get("q", "").strip()
    autor_id = request.GET.get("autor", "")
    categoria_id = request.GET.get("categoria", "")

    livros = Livro.objects.select_related(
        "autor", "categoria"
    ).all()

    if pesquisa:
        livros = livros.filter(
            titulo__icontains=pesquisa
        )

    if autor_id:
        livros = livros.filter(autor_id=autor_id)

    if categoria_id:
        livros = livros.filter(categoria_id=categoria_id)

    livros = livros.order_by("titulo")

    paginator = Paginator(livros, 5)

    numero_pagina = request.GET.get("page")

    pagina_atual = paginator.get_page(numero_pagina)

    contexto = {
        "livros": pagina_atual,
        "pagina_atual": pagina_atual,
        "pesquisa": pesquisa,
        "autor_selecionado": autor_id,
        "categoria_selecionada": categoria_id,
        "autores": Autor.objects.all().order_by("nome"),
        "categorias": Categoria.objects.all().order_by("nome"),
    }

    return render(
        request,
        "core/lista_livros.html",
        contexto
    )
