# Generated by Django 5.1.1 on 2024-11-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0013_alter_device_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='device',
            name='modelo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='device',
            name='tarjetaVideo',
            field=models.CharField(blank=True, default='some string', max_length=200, null=True, verbose_name='Tarjeta de Video'),
        ),
    ]
