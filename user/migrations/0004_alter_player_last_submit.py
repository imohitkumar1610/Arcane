# Generated by Django 3.2.7 on 2021-09-26 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_player_last_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_submit',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 26, 21, 24, 38, 732704)),
        ),
    ]