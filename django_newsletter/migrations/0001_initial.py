# Generated by Django 3.2.8 on 2021-11-13 11:36

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_domain', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailMessageCron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('send_to_confirmed', models.BooleanField(default=True)),
                ('send_to_not_confirmed', models.BooleanField(default=False)),
                ('cron', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailMessageMembershipTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('send_to_confirmed', models.BooleanField(default=True)),
                ('send_to_not_confirmed', models.BooleanField(default=False)),
                ('days_from_join', models.IntegerField(blank=True, default=0, help_text='Number of days spend from join to send this message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailMessageToDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('send_to_confirmed', models.BooleanField(default=True)),
                ('send_to_not_confirmed', models.BooleanField(default=False)),
                ('send_time', models.DateTimeField()),
                ('is_send', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=50)),
                ('join_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_domain', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
