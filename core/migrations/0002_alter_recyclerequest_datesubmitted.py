# Generated by Django 3.2.16 on 2022-10-29 17:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclerequest',
            name='dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 17, 34, 31, 511746, tzinfo=utc)),
        ),
    ]