from rest_framework import generics, permissions

from apps.charging.models import ChargingStation
from apps.charging.serializers import ChargingStationSerializer


# api/charging-stations
class ChargingStationView(generics.ListCreateAPIView):
    serializer_class = ChargingStationSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        is_available = self.request.query_params.get("is_available")
        queryset = ChargingStation.objects.all()

        if is_available:
            queryset = queryset.filter(is_available=is_available)
        return queryset
