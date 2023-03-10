from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.charging.models import Charger, ChargingStation
from apps.charging.serializers import ChargerSerializer, ChargingStationSerializer


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


# api/charging-stations/<int:charging_station_id>
class ChargingStationDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "charging_station_id"

    queryset = ChargingStation.objects.all()
    serializer_class = ChargingStationSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]


# api/charging-stations/<int:charging_station_id>/chargers
class ChargerView(generics.ListCreateAPIView):
    serializer_class = ChargerSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Charger.objects.filter(charging_station=self.kwargs["charging_station_id"])
        is_available = self.request.query_params.get("is_available")
        type = self.request.query_params.get("type")

        if is_available:
            queryset = queryset.filter(is_available=is_available)
        if type:
            queryset = queryset.filter(type=type)
        return queryset

    def create(self, request, *args, **kwargs):
        charging_station_id = kwargs.get("charging_station_id")
        mutable_data = request.data.copy()
        mutable_data["charging_station"] = charging_station_id
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# api/charging-stations/<int:charging_station_id>/chargers/<int:charger_id>
class ChargerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def get_object(self):
        queryset = self.get_queryset()
        charger_id = self.kwargs["charger_id"]
        charger = get_object_or_404(queryset, id=charger_id, charging_station_id=self.kwargs["charging_station_id"])
        return charger

    def patch(self, request, *args, **kwargs):
        charger = self.get_object()
        serializer = self.get_serializer(charger, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_at=timezone.now())
        return Response(serializer.data)
