# Generated by Django 5.1.1 on 2024-11-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0015_alter_device_mouses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='area',
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Apellidos y Nombres'),
        ),
        migrations.AddField(
            model_name='worker',
            name='area',
            field=models.ManyToManyField(to='devices.area', verbose_name='Areas'),
        ),
    ]
