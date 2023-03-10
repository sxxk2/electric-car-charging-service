from rest_framework import serializers

from .models import Coupon


# api/coupons
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
        read_only_fields = ["id", "issuer", "code", "used_at", "used_by", "created_at"]
