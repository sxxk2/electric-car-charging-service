from django.conf import settings
from django.db import models
from django.utils import timezone


class Coupon(models.Model):
    issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=15)
    balance = models.PositiveIntegerField()
    used_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="used_coupons"
    )
    used_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def is_available(self):
        return self.used_at is None and timezone.now() < self.expired_at

    class Meta:
        db_table = "coupons"
