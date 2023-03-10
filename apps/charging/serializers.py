from rest_framework import serializers

from apps.charging.models import ChargingStation


# api/charging-stations
class ChargingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStation
        fields = "__all__"
