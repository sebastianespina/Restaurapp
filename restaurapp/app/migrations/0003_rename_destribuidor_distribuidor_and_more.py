# Generated by Django 4.1 on 2022-09-27 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contacto_alter_destribuidor_correo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Destribuidor',
            new_name='Distribuidor',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='destribuidor',
            new_name='distribuidor',
        ),
    ]
