# Generated by Django 4.0.4 on 2022-10-17 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_username_material_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='user',
        ),
        migrations.AlterField(
            model_name='recyclerequest',
            name='dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 0, 13, 159475)),
        ),
    ]