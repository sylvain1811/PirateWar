# Generated by Django 2.0.2 on 2018-04-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirateWarApp', '0006_auto_20180402_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
