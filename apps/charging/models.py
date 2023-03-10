from django.db import models

from apps.utils.timestamp import TimeStampedModel


class ChargingStation(TimeStampedModel):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="위도")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="경도")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "charging_stations"


class Charger(TimeStampedModel):
    class ChargerTypeChoices(models.TextChoices):
        FAST = "fast", "급속"
        SLOW = "slow", "완속"

    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE, related_name="chargers")
    type = models.CharField(max_length=20, choices=ChargerTypeChoices.choices)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.type
