# Generated by Django 2.2.12 on 2020-05-14 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_auto_20200514_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='idTipoDocu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.TipoDocu', verbose_name='Identificador del tipo de documento'),
        ),
    ]
