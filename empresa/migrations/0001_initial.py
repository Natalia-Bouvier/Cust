# Generated by Django 3.0.4 on 2020-03-24 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(default='rut de la empresa', max_length=25)),
                ('razon_social', models.CharField(default='razón social de la empresa', max_length=50)),
                ('direccion', models.CharField(default='Dirección de la empresa', max_length=200)),
                ('telefono', models.CharField(default='Teléfono de la empresa', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=35)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(default='Dirección del cliente', max_length=200)),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10)),
                ('telefono', models.CharField(default='Teléfono del cliente', max_length=9)),
                ('correo', models.EmailField(default='example@email.com', max_length=255)),
                ('cedula', models.CharField(default='1.111.111-1', max_length=15)),
                ('Observaciones', models.CharField(default='', max_length=1000)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.Empresa')),
            ],
        ),
    ]
