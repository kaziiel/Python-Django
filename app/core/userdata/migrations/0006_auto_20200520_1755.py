# Generated by Django 2.2.12 on 2020-05-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20200514_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='FotoUser',
            field=models.ImageField(default='user.png', upload_to='img/perfil', verbose_name='Foto de perfil'),
        ),
    ]
