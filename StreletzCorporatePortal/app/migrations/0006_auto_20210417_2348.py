# Generated by Django 3.1.7 on 2021-04-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210417_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='worksSince',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
