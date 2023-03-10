from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.payment.models import PaymentMethod
from apps.payment.serializers import PaymentMethodSerializer


# api/payment-methods
class PaymentMethodView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentMethodSerializer

    def get_queryset(self):
        type = self.request.query_params.get("type")
        queryset = PaymentMethod.objects.filter(user_id=self.request.user)

        if type:
            queryset = queryset.filter(type=type)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
