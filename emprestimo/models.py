from django.db import models
from usuarios.models import Usuario
from funcionarios.models import Funcionario
from acervo.models import Livro
import uuid



# Create your models here.
class Emprestimo(models.Model):
    ordem_emprestimo = uuid.uuid4()
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    fk_funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    fk_livro1 = models.ForeignKey(Livro, related_name='livro1', blank=False, null=False, on_delete=models.DO_NOTHING)
    fk_livro2 = models.ForeignKey(Livro, related_name='livro2', blank=True, null=True, on_delete=models.DO_NOTHING)
    fk_livro3 = models.ForeignKey(Livro, related_name='livro3', blank=True, null=True, on_delete=models.DO_NOTHING)
    fk_livro4 = models.ForeignKey(Livro, related_name='livro4', blank=True, null=True, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ordem_emprestimo} - {self.fk_usuario} - {self.data_emprestimo}'
