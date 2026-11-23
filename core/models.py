from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name="livros",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="livros",
    )
    ano_publicacao = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo