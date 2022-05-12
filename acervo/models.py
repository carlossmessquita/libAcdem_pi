from django.db import models


# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=8, blank=False, null=False, editable=True)
    rua = models.CharField(max_length=120, blank=False, null=False, editable=True)
    numero = models.CharField(max_length=6, blank=False, null=False, editable=True)
    bairro = models.CharField(max_length=50, blank=False, null=False, editable=True)
    cidade = models.CharField(max_length=50, blank=False, null=False, editable=True)

    def __str__(self):
        endereco = f'Editora: {self.rua}, {self.numero}, {self.cep}, {self.bairro}, {self.cidade}'
        return endereco.title()


class Editora(models.Model):
    fk_endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    cnpj = models.CharField(max_length=15, null=False, blank=False, editable=True)
    razao_social = models.CharField(max_length=150, null=False, blank=False, editable=True)
    nome_fantasia = models.CharField(max_length=150, null=False, blank=False, editable=True)
    telefone1 = models.CharField(max_length=15, null=False, blank=False, editable=True)
    telefone2 = models.CharField(max_length=15, null=True, blank=True, editable=True)
    email = models.EmailField(max_length=150, null=False, blank=False, editable=True)

    def __str__(self):
        return f'Editora {self.nome_fantasia}'


class Autor(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, editable=True)
    nome_do_meio = models.CharField(max_length=50, blank=True, null=True, editable=True)
    sobrenome = models.CharField(max_length=50, blank=False, null=False, editable=True)

    def __str__(self):
        return f'{self.sobrenome}, {self.nome}'


class Livro(models.Model):
    fk_editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)
    fk_autor = models.ForeignKey(Autor, related_name='autor', blank=False, null=False, on_delete=models.DO_NOTHING)
    fk_coautor = models.ForeignKey(Autor, related_name='coautor',blank=True, null=True, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=150, blank=False, null=False, editable=True)
    subtitulo = models.CharField(max_length=200, blank=True, null=True, editable=True)
    isbn = models.CharField(max_length=100, blank=False, null=False, editable=True)
    categoria = models.CharField(max_length=100, blank=False, null=False)
    subcategoria = models.CharField(max_length=100, blank=True, null=True)
    edicao = models.IntegerField()
    ano_lancamento = models.DateField()

    def __str__(self):
        return f'"{self.titulo}", {self.fk_autor}'
