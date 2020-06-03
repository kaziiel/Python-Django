# Generated by Django 2.2.12 on 2020-05-13 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20200513_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cateproye',
            old_name='MorotDB',
            new_name='MotorDB',
        ),
        migrations.AlterField(
            model_name='documentos',
            name='idTipoDocu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.TipoDocu', verbose_name='Identificador del tipo de documento'),
        ),
    ]
