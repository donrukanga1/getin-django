# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PregnantGirl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[(b'Single', b'Single'), (b'Married', b'Married'), (b'Divorced/Separated', b'Divorced/Separated'), (b'Widowed', b'Widowed')], max_length=255)),
                ('education_level', models.CharField(choices=[(b'None', b'None'), (b'Primary', b'Primary'), (b'Secondary', b'Secondary'), (b'Tertiary', b'Tertiary')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
