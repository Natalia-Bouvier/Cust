# Generated by Django 2.2.6 on 2020-03-18 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0008_auto_20200317_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo_de_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.CategoriaServicio'),
        ),
    ]
