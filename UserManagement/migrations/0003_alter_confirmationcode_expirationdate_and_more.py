# Generated by Django 4.0.4 on 2022-10-17 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_alter_confirmationcode_expirationdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 56, 53, 933987)),
        ),
        migrations.AlterField(
            model_name='locationcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 56, 53, 939356)),
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 56, 53, 936488)),
        ),
        migrations.AlterField(
            model_name='twofactorauthcode',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 22, 56, 53, 938087)),
        ),
    ]