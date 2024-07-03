# Generated by Django 5.0 on 2024-06-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("insbiz", "0004_doctor_hospital_doctor_speciality_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="level",
            field=models.CharField(
                choices=[("3", "Level-3"), ("4", "Level-4")], max_length=225, null=True
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="year",
            field=models.CharField(
                choices=[
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                    ("6", "6"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
