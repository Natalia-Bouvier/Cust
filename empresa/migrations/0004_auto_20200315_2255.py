# Generated by Django 3.0.3 on 2020-03-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20200313_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
