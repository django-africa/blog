# Generated by Django 3.0.7 on 2020-08-30 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApi', '0015_auto_20200830_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]