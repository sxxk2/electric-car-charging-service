from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.user.urls")),
    path("api/", include("apps.coupon.urls")),
    path("api/", include("apps.charging.urls")),
    path("api/", include("apps.payment.urls")),
]
