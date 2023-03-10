from rest_framework import serializers

from .models import Coupon


# api/coupons
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
        read_only_fields = ["id", "issuer", "code", "used_at", "used_by", "created_at"]


# api/coupons/register
class CouponRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ["id", "code", "balance", "used_by", "used_at", "created_at", "expired_at"]
        read_only_fields = ["id", "balance", "used_by", "used_at", "created_at", "expired_at"]
