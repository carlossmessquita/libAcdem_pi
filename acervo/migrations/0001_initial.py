# Generated by Django 3.2 on 2022-05-09 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nome_do_meio', models.CharField(blank=True, max_length=50, null=True)),
                ('sobrenome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=15)),
                ('razao_social', models.CharField(max_length=150)),
                ('nome_fantasia', models.CharField(max_length=150)),
                ('telefone1', models.CharField(max_length=15)),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
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
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(blank=True, max_length=200, null=True)),
                ('isbn', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('subcategoria', models.CharField(blank=True, max_length=100, null=True)),
                ('edicao', models.IntegerField()),
                ('ano_lancamento', models.DateField()),
                ('fk_autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='autor', to='acervo.autor')),
                ('fk_coautor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='coautor', to='acervo.autor')),
                ('fk_editora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='acervo.editora')),
            ],
        ),
        migrations.AddField(
            model_name='editora',
            name='fk_endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='acervo.endereco'),
        ),
    ]