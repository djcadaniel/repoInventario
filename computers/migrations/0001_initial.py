# Generated by Django 5.1.1 on 2024-10-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7, verbose_name='Codigo')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=200, verbose_name='Modelo')),
                ('serie', models.CharField(max_length=200, verbose_name='Serie')),
                ('procesador', models.CharField(max_length=200, verbose_name='Procesador')),
                ('ram', models.CharField(max_length=200, verbose_name='RAM')),
                ('discoduro', models.CharField(max_length=200, verbose_name='Disco Duro')),
                ('video', models.CharField(max_length=200, verbose_name='Tarjeta de Video')),
                ('observaciones', models.CharField(max_length=1000, verbose_name='Observaciones')),
                ('garantia', models.CharField(max_length=1000, verbose_name='Garantía')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('area', models.CharField(max_length=50, verbose_name='Área')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'ordering': ['-created'],
            },
        ),
    ]
