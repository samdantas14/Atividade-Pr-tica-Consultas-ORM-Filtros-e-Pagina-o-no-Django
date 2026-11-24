from django.shortcuts import render
from .models import Livro

def lista_livros(request):
    livros = Livro.objects.select_related("autor", "categoria").all()

    pesquisa = request.GET.get("q")

    if pesquisa:
        livros = livros.filter(titulo__icontains=pesquisa)

    return render(
        request,
        "core/lista_livros.html",
        {
            "livros": livros,
            "pesquisa": pesquisa,
        },
    )

def lista_livros(request):
    livros = Livro.objects.select_related("autor", "categoria").all()

    return render(
        request,
        "core/lista_livros.html",
        {"livros": livros},
    )