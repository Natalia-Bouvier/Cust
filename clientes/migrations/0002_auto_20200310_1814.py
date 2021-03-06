# Generated by Django 2.2.6 on 2020-03-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(default='example@email.com', max_length=255),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default='Dirección del cliente', max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Femenino'), (2, 'Masculino')], default=1),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default='Teléfono del cliente', max_length=9),
        ),
    ]
