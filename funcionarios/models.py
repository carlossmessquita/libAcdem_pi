from django.db import models


# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=8, blank=False, null=False, editable=True)
    rua = models.CharField(max_length=120, blank=False, null=False, editable=True)
    numero = models.CharField(max_length=6, blank=False, null=False, editable=True)
    bairro = models.CharField(max_length=50, blank=False, null=False, editable=True)
    cidade = models.CharField(max_length=50, blank=False, null=False, editable=True)

    def __str__(self):
        endereco = f'{self.rua}, {self.numero}, {self.cep}, {self.bairro}, {self.cidade}'
        return endereco.title()


# Create your models here.
class Funcionario(models.Model):
    fk_endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50, blank=False, null=False, editable=True)
    sobrenome = models.CharField(max_length=50, blank=False, null=False, editable=True)
    email = models.EmailField(max_length=100, blank=False, null=False, editable=True)
    telefone1 = models.CharField(max_length=15, null=False, blank=False, editable=True)
    telefone2 = models.CharField(max_length=15, null=True, blank=True, editable=True)
    senha = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return f'{self.nome}, {self.sobrenome}'
