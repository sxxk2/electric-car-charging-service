from django.db import models

from apps.user.models import User
from apps.utils.timestamp import TimeStampedModel


class PaymentMethod(TimeStampedModel):
    class PaymentMethodChoices(models.TextChoices):
        CARD = "card", "신용카드"
        BANK_TRANSFER = "bank_transfer", "계좌이체"

    class BankChoices(models.TextChoices):
        KOOKMIN = "kookmin", "KB국민은행"
        SHINHAN = "shinhan", "신한은행"
        WOORI = "woori", "우리은행"
        KEBHANA = "hana", "KEB하나은행"
        NH = "nh", "농협"
        CITY = "city", "시티은행"
        KAKAO = "kakao", "카카오뱅크"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_methods")
    type = models.CharField(max_length=20, choices=PaymentMethodChoices.choices)
    card_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    bank_name = models.CharField(max_length=20, null=True, blank=True, choices=BankChoices.choices)
    bank_account = models.CharField(max_length=50, null=True, blank=True, unique=True)

    class Meta:
        db_table = "payment_methods"
