# Generated by Django 3.2.8 on 2021-11-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_newsletter', '0004_member_previous_confirmed_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='previous_confirmed_state',
        ),
        migrations.AlterField(
            model_name='member',
            name='join_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
