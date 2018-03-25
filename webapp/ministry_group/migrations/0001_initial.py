# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_members', '0006_auto_20180325_0304'),
    ]

    operations = [
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
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry', to='ministry_group.Ministry')),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ministry_type', to='ministry_group.MinistryType'),
        ),
    ]
