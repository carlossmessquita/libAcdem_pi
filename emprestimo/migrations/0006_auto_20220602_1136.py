# Generated by Django 3.2 on 2022-06-02 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0005_auto_20220512_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(auto_created=True, default=datetime.date(2022, 6, 2), editable=False),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='prazo',
            field=models.DateField(auto_created=True, default=datetime.date(2022, 6, 17), editable=False),
        ),
    ]
