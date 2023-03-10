from django.urls import path

from apps.coupon.views import CouponView

urlpatterns = [
    path("", CouponView.as_view(), name="coupon"),
]
