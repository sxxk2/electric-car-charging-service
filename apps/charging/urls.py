from django.urls import path

from apps.charging.views import ChargerView, ChargingStationDetailView, ChargingStationView

app_name = "charging"

urlpatterns = [
    path("charging-stations", ChargingStationView.as_view(), name="charging_station"),
    path(
        "charging-stations/<int:charging_station_id>",
        ChargingStationDetailView.as_view(),
        name="charging_station_detail",
    ),
    path("charging-stations/<int:charging_station_id>/chargers", ChargerView.as_view(), name="charger"),
]
