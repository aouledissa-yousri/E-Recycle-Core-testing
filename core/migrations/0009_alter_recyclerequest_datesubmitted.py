# Generated by Django 4.0.4 on 2022-10-20 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_citizen_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclerequest',
            name='dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 20, 10, 42, 16, 807475, tzinfo=utc)),
        ),
    ]