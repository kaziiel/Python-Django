# Generated by Django 2.2.12 on 2020-05-13 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20200513_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='idTipoDocu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.TipoDocu', verbose_name='Identificador del tipo de documento'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='FechaFin',
            field=models.DateField(auto_now=True, null=True, verbose_name='Terminado el'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='FechaIni',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Iniciado el'),
        ),
    ]
