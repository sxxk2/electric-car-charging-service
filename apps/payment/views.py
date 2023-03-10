from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.payment.models import PaymentMethod
from apps.payment.serializers import PaymentMethodSerializer
from apps.utils.permissions import IsOwner


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


# api/payment-methods/<int:payment_method_id>
class PaymentMethodDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PaymentMethodSerializer
    # queryset = PaymentMethod.objects.all()

    def get_queryset(self):
        queryset = PaymentMethod.objects.filter(user_id=self.request.user)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs["payment_method_id"])
        return obj
