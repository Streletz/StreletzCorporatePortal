# Generated by Django 3.1.7 on 2021-05-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210503_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='worksSince',
            field=models.DateTimeField(),
        ),
        migrations.RunSQL("ALTER TABLE app_employee ALTER COLUMN \"created\" SET DEFAULT now() "),
        migrations.RunSQL("ALTER TABLE app_employee ALTER COLUMN \"worksSince\" SET DEFAULT now() ")
    ]