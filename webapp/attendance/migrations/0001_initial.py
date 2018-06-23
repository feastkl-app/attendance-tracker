# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-26 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_members', '0006_auto_20180325_0304'),
        ('events', '0002_auto_20180426_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('attended', models.NullBooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events.Event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='account_members.MemberProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
