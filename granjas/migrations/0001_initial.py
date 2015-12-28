# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Corrale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=255)),
                ('area_disponible', models.CharField(max_length=255)),
                ('capacidad', models.CharField(max_length=255)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Galpone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Granja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=11)),
                ('ubicacion', models.CharField(max_length=255)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('dueno', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Granjas_tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmunocastracione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rastro', models.CharField(max_length=11, blank=True)),
                ('periodo_venta', models.CharField(max_length=11, blank=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('granja', models.ForeignKey(to='granjas.Granja')),
            ],
        ),
        migrations.CreateModel(
            name='Inmunocastraciones_extendida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=50)),
                ('fecha_aplicacion', models.CharField(max_length=10, blank=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('Inmunocastracion', models.ForeignKey(to='granjas.Inmunocastracione')),
            ],
        ),
        migrations.AddField(
            model_name='granja',
            name='tipo_granja',
            field=models.ForeignKey(blank=True, to='granjas.Granjas_tipo', null=True),
        ),
    ]
