# Generated by Django 3.0.4 on 2020-03-27 01:35

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
                ('rut', models.CharField(max_length=25, null=True)),
                ('razon_social', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=35)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10)),
                ('telefono', models.CharField(max_length=9, null=True)),
                ('correo', models.EmailField(max_length=255, null=True)),
                ('cedula', models.CharField(max_length=15, null=True)),
                ('Observaciones', models.CharField(default='', max_length=1000)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.Empresa')),
            ],
        ),
    ]
