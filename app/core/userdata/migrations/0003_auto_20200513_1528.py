# Generated by Django 2.2.12 on 2020-05-13 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200507_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='addData',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='apelUser',
            field=models.CharField(max_length=256, null=True, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='geneUser',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Maculino', 'Masculino'), ('Otro', 'Otro')], default='Otro', max_length=20, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='modifiat',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='nombUser',
            field=models.CharField(max_length=256, null=True, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='profeUser',
            field=models.CharField(max_length=100, null=True, verbose_name='Profesión'),
        ),
        migrations.AddField(
            model_name='habiluser',
            name='Prof',
            field=models.CharField(max_length=100, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='TeleUser',
            field=models.CharField(max_length=20, verbose_name='Número de Teléfono'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='UserDNI',
            field=models.CharField(max_length=20, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='addUser',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='estaRol',
            field=models.CharField(max_length=10, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='idRole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.Roles', verbose_name='Identificador de Rol'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Identificador de Usuario'),
        ),
        migrations.AlterField(
            model_name='detaroles',
            name='udtUser',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificador el'),
        ),
        migrations.AlterField(
            model_name='habiluser',
            name='NombHabil',
            field=models.CharField(max_length=100, verbose_name='Competencia'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='idHabil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.HabilUser', verbose_name='Identificador de Habilidad'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Identificador de Usuario'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='pcrHabil',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Porcentaje'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='udtHabil',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=''),
        ),
    ]
