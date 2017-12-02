# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-02 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_auto_20171202_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('portaOberta', models.NullBooleanField()),
                ('contrasenyaValida', models.NullBooleanField()),
                ('usuari', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.Profile')),
            ],
        ),
    ]
