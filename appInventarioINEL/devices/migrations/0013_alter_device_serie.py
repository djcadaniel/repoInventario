# Generated by Django 5.1.1 on 2024-11-25 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_audifono_camera_cooler_keyboard_monitor_stabilizer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serie',
            field=models.CharField(blank=True, default='SOME STRING', max_length=200, null=True, verbose_name='Serie'),
        ),
    ]
