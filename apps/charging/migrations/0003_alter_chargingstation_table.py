# Generated by Django 4.1.6 on 2023-03-10 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("charging", "0002_alter_chargingstation_name"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="chargingstation",
            table="charging_stations",
        ),
    ]
