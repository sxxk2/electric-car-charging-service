from django.urls import path

from apps.coupon.views import CouponDetailView, CouponRegisterView, CouponView

app_name = "coupon"

urlpatterns = [
    path("", CouponView.as_view(), name="coupon"),
    path("/<int:coupon_id>", CouponDetailView.as_view(), name="coupon_detail"),
    path("/register", CouponRegisterView.as_view(), name="coupon_register"),
]
