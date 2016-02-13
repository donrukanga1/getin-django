# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregnantgirl',
            options={'verbose_name_plural': 'Pregnant Girls'},
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='has_gone_for_anc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='latitude',
            field=models.FloatField(default=-0.8195),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='longitude',
            field=models.FloatField(default=29.7426),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='number_of_children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='parish',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='prefered_language',
            field=models.CharField(choices=[(b'English', b'English'), (b'Luganda', b'Luganda')], default=b'English', max_length=50),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='subcounty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pregnantgirl',
            name='village',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]