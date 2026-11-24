
from django.db import migrations


def completar_catalogo(apps, schema_editor):
    Livro = apps.get_model("core", "Livro")
    Autor = apps.get_model("core", "Autor")
    Categoria = apps.get_model("core", "Categoria")

    autores = list(Autor.objects.order_by("id"))
    categorias = list(Categoria.objects.order_by("id"))

    if not autores or not categorias:
        return

    exemplos = [
        ("A viagem inesperada", 2018),
        ("Mistérios da biblioteca", 2020),
        ("O caminho das estrelas", 2015),
        ("Memórias de um verão", 2012),
        ("A última página", 2021),
        ("Entre sonhos e realidade", 2019),
        ("O segredo do jardim", 2016),
        ("Uma nova jornada", 2022),
        ("Histórias do passado", 2014),
        ("O universo desconhecido", 2023),
        ("Além das montanhas", 2017),
    ]

    quantidade_atual = Livro.objects.count()

    for indice, (titulo, ano) in enumerate(exemplos):
        if quantidade_atual >= 20:
            break

        Livro.objects.get_or_create(
            titulo=titulo,
            defaults={
                "ano_publicacao": ano,
                "descricao": "Livro de exemplo para demonstrar a pesquisa, os filtros e a paginação.",
                "autor": autores[indice % len(autores)],
                "categoria": categorias[indice % len(categorias)],
            },
        )

        quantidade_atual = Livro.objects.count()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            completar_catalogo,
            migrations.RunPython.noop
        ),
    ]
