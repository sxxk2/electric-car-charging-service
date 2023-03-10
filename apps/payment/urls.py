from django.urls import path

from apps.payment.views import PaymentMethodView

app_name = "payment"

urlpatterns = [
    path("payment-methods", PaymentMethodView.as_view(), name="payment_methods"),
]
