from django.urls import path

from apps.charging.views import ChargingStationView

app_name = "charging"

urlpatterns = [
    path("charging-stations", ChargingStationView.as_view(), name="charging_station"),
]
