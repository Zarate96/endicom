# Generated by Django 3.2.8 on 2021-10-19 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211018_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
