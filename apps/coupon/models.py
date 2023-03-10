from django.db import models
from django.utils import timezone

from apps.user.models import User


class Coupon(models.Model):
    issuer = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=15)
    balance = models.PositiveIntegerField()
    used_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="used_coupons")
    used_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def is_available(self):
        return self.used_at is None and timezone.now() < self.expired_at

    class Meta:
        db_table = "coupons"
