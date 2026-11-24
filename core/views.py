from django.shortcuts import render

from .models import Livro


def lista_livros(request):
    livros = Livro.objects.select_related("autor", "categoria").all()

    return render(
        request,
        "core/lista_livros.html",
        {"livros": livros},
    )