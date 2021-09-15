# Generated by Django 3.2 on 2021-05-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_usermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='facility_type',
            field=models.CharField(choices=[('Oxygen', 'OXYGEN'), ('CovidBed', 'COVID BED'), ('CovidTest', 'COVID TESTING'), ('DoctorOnCall', 'DOCTOR ON CALL'), ('Ambulance', 'AMBULANCE'), ('Food', 'FOOD'), ('Medicine', 'MEDICINE')], default=None, max_length=15),
        ),
    ]