from django.urls import path

from apps.coupon.views import CouponRegisterView, CouponView

app_name = "coupon"

urlpatterns = [
    path("", CouponView.as_view(), name="coupon"),
    path("/register", CouponRegisterView.as_view(), name="coupon_register"),
]
