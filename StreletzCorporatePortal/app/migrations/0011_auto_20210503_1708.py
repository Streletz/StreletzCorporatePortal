# Generated by Django 3.1.7 on 2021-05-03 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210503_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 17, 8, 47, 238885)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='worksSince',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 17, 8, 47, 238885)),
        ),
        migrations.RunSQL("ALTER TABLE app_post ALTER COLUMN \"created\" SET DEFAULT now() ")
    ]
