import uuid

from rest_framework import generics, permissions

from apps.coupon.models import Coupon
from apps.coupon.serializers import CouponSerializer


# api/coupons
class CouponView(generics.ListCreateAPIView):
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Coupon.objects.all()
        return queryset

    def perform_create(self, serializer):
        code = str(uuid.uuid4()).replace("-", "")[:15]
        serializer.save(issuer=self.request.user, code=code)
