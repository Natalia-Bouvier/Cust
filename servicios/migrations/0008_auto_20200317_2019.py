# Generated by Django 2.2.6 on 2020-03-17 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_auto_20200315_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo_de_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.CategoriaServicio'),
        ),
    ]