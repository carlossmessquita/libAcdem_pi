# Generated by Django 3.2 on 2022-05-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_auto_20220512_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='prazo',
            field=models.DateField(auto_created=True, default='27/05/2022'),
        ),
    ]
