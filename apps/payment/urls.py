from django.urls import path

from apps.payment.views import PaymentMethodDetailView, PaymentMethodView

app_name = "payment"

urlpatterns = [
    path("payment-methods", PaymentMethodView.as_view(), name="payment_methods"),
    path("payment-methods/<int:payment_method_id>", PaymentMethodDetailView.as_view(), name="payment_methods_detail"),
]
