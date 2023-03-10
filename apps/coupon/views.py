import uuid

from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.coupon.models import Coupon
from apps.coupon.serializers import CouponRegisterSerializer, CouponSerializer


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


# api/coupons/register
class CouponRegisterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        code = request.data.get("code")
        if not code:
            return Response({"message": "쿠폰번호를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)

        coupon = Coupon.objects.get(code=code)
        if not coupon.is_available():
            return Response({"message": "사용할 수 없는 쿠폰입니다."}, status=status.HTTP_400_BAD_REQUEST)

        coupon.used_by = request.user
        coupon.used_at = timezone.now()
        coupon.save()

        return Response(CouponRegisterSerializer(coupon).data)
