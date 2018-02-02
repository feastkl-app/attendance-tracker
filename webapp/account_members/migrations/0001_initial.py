# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-02 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(blank=True, max_length=32)),
                ('lastname', models.CharField(blank=True, max_length=32)),
                ('middlename', models.CharField(blank=True, max_length=32)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=8)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=16)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=8)),
                ('member_since', models.DateField(blank=True, null=True)),
                ('active_member', models.BooleanField(default=True)),
                ('location', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Feast Members',
            },
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32)),
                ('remarks', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinistryMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry_member', to='account_members.MemberProfile')),
                ('member_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry_member_type', to='account_members.MemberProfile')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry', to='account_members.Ministry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinistryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32)),
                ('remarks', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ministry',
            name='ministry_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry', to='account_members.MinistryType'),
        ),
    ]
