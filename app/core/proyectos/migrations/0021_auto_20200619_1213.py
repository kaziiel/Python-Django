# Generated by Django 2.2.12 on 2020-06-19 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0020_auto_20200521_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='idTipoDocu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.TipoDocu', verbose_name='Identificador del tipo de documento'),
        ),
    ]
