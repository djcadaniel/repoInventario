# Generated by Django 5.1.1 on 2024-11-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_processor_remove_device_procesador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='serie',
            field=models.CharField(default='SOME STRING', max_length=200, verbose_name='Serie'),
        ),
    ]
