# Generated by Django 3.0.3 on 2020-03-19 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0014_auto_20200319_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo_de_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.CategoriaServicio'),
        ),
    ]
