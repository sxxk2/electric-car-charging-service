from django.urls import path

from apps.coupon.views import CouponDetailView, CouponRegisterView, CouponView

app_name = "coupon"

urlpatterns = [
    path("coupons", CouponView.as_view(), name="coupon"),
    path("coupons/<int:coupon_id>", CouponDetailView.as_view(), name="coupon_detail"),
    path("coupons/register", CouponRegisterView.as_view(), name="coupon_register"),
]
