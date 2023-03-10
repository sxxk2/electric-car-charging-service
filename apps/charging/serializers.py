from rest_framework import serializers

from apps.charging.models import Charger, ChargingStation


# api/charging-stations
class ChargingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStation
        fields = "__all__"


# api/charging-stations/<int:charging_station_id>/chargers
class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = "__all__"
