# Generated by Django 4.0.4 on 2022-10-17 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 4, 11, 774402)),
        ),
        migrations.AlterField(
            model_name='locationcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 4, 11, 778972)),
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 4, 11, 776873)),
        ),
        migrations.AlterField(
            model_name='twofactorauthcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 4, 11, 777943)),
        ),
    ]
