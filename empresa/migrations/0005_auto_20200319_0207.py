# Generated by Django 3.0.3 on 2020-03-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20200315_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10),
        ),
    ]
