# Generated by Django 3.0.4 on 2020-03-14 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
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
        migrations.RemoveField(
            model_name='categoriaservicio',
            name='tiposervicio',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='Colaborador',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='Nombre',
        ),
        migrations.AddField(
            model_name='categoriaservicio',
            name='tipo_de_servicio',
            field=models.CharField(default='servicio', max_length=20),
        ),
        migrations.AddField(
            model_name='servicio',
            name='fecha_hora',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo_de_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.CategoriaServicio'),
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=35)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('direccion', models.CharField(default='Dirección del cliente', max_length=200)),
                ('sexo', models.IntegerField(choices=[(1, 'Femenino'), (2, 'Masculino')], default=1)),
                ('telefono', models.CharField(default='Teléfono del cliente', max_length=9)),
                ('correo', models.EmailField(default='example@email.com', max_length=255)),
                ('cedula', models.CharField(default='1.111.111-1', max_length=15)),
                ('Observaciones', models.CharField(default='', max_length=1000)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=35)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('direccion', models.CharField(default='Dirección del cliente', max_length=200)),
                ('sexo', models.IntegerField(choices=[(1, 'Femenino'), (2, 'Masculino')], default=1)),
                ('telefono', models.CharField(default='Teléfono del cliente', max_length=9)),
                ('correo', models.EmailField(default='example@email.com', max_length=255)),
                ('cedula', models.CharField(default='1.111.111-1', max_length=15)),
                ('observaciones', models.CharField(default='', max_length=1000)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='categoriaservicio',
            name='Empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Empresa'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Cliente'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='colaborador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.Colaborador'),
        ),
    ]