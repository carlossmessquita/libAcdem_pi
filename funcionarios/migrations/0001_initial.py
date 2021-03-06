# Generated by Django 3.2 on 2022-05-12 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=120)),
                ('numero', models.CharField(max_length=6)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefone1', models.CharField(max_length=15)),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True)),
                ('senha', models.CharField(max_length=8)),
                ('fk_endereco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='funcionarios.endereco')),
            ],
        ),
    ]
