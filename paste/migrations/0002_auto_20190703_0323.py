# Generated by Django 2.2.3 on 2019-07-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paste',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
