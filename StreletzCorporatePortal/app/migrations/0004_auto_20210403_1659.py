# Generated by Django 3.1.7 on 2021-04-03 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210313_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 16, 59, 41, 88847)),
        ),
    ]
