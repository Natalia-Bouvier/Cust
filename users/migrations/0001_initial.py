# Generated by Django 3.0.4 on 2020-03-27 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Nombre', models.CharField(default='', max_length=35)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(default='Dirección del cliente', max_length=200)),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10)),
                ('telefono', models.CharField(default='Teléfono del cliente', max_length=9)),
                ('correo', models.EmailField(default='', max_length=255, unique=True, verbose_name='correo electronico')),
                ('cedula', models.CharField(default='1.111.111-1', max_length=15)),
                ('Observaciones', models.CharField(default='', max_length=1000)),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('staff', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=True)),
                ('groups', models.IntegerField(default=0)),
                ('user_permissions', models.IntegerField(default=0)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.Empresa')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]
