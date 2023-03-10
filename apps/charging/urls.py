from django.urls import path

from apps.charging.views import ChargerView, ChargingStationView

app_name = "charging"

urlpatterns = [
    path("charging-stations", ChargingStationView.as_view(), name="charging_station"),
    path("charging-stations/<int:charging_station_id>/chargers", ChargerView.as_view(), name="charger"),
]
