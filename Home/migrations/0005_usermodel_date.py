# Generated by Django 3.2 on 2021-05-01 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_usermodel_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
