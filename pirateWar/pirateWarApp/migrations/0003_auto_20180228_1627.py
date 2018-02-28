# Generated by Django 2.0.2 on 2018-02-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirateWarApp', '0002_auto_20180226_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship',
            name='currentActivity',
        ),
        migrations.AlterField(
            model_name='ship',
            name='cannon',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ship',
            name='crew',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ship',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ship',
            name='life',
            field=models.IntegerField(default=100),
        ),
    ]
