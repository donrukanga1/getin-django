# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=18)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[(b'admin', b'admin'), (b'vht', b'vht'), (b'midwife', b'midwife'), (b'dho', b'dho')], max_length=120)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='AntenatalVist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField()),
                ('services', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('emergency_contact', models.CharField(default=b'', max_length=32)),
                ('contact_type', models.CharField(choices=[(b'Parent', b'Parent'), (b'Guardian', b'Guardian'), (b'Spouse', b'Spouse'), (b'Sibling', b'Sibling')], default=b'Parent', max_length=20)),
                ('contact_number', models.CharField(default=b'', max_length=13)),
                ('number_of_children', models.IntegerField(default=0)),
                ('has_gone_for_anc', models.BooleanField(default=False)),
                ('prefered_language', models.CharField(choices=[(b'English', b'English'), (b'Luganda', b'Luganda')], default=b'English', max_length=50)),
                ('village', models.CharField(blank=True, max_length=50, null=True)),
                ('parish', models.CharField(blank=True, max_length=50, null=True)),
                ('subcounty', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.FloatField(default=-0.8195)),
                ('longitude', models.FloatField(default=29.7426)),
            ],
            options={
                'verbose_name_plural': 'Pregnant Girls',
            },
        ),
        migrations.CreateModel(
            name='PresetMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=160)),
            ],
        ),
        migrations.AddField(
            model_name='antenatalvist',
            name='girl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.PregnantGirl'),
        ),
    ]
