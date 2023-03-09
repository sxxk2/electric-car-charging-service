from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.utils.timestamp import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=8, unique=True)
    balance = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "users"


class PaymentMethod(TimeStampedModel):
    class PaymentMethodChoices(models.TextChoices):
        CARD = "card", "신용카드"
        BANK_TRANSFER = "bank_transfer", "계좌이체"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_methods")
    payment_method = models.CharField(max_length=20, choices=PaymentMethodChoices.choices)
    card_number = models.CharField(max_length=20, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    bank_account = models.CharField(max_length=50, null=True, blank=True)
