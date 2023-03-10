from rest_framework import serializers

from apps.payment.models import PaymentMethod


# api/payment-methods
class PaymentMethodSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get("type") == "card":
            if data.get("bank_name") or data.get("bank_account"):
                raise serializers.ValidationError("잘못된 결제 수단입니다.")
            elif data.get("card_number") is None:
                raise serializers.ValidationError("카드 번호를 입력해 주세요.")

        elif data.get("type") == "bank_transfer":
            if data.get("card_number"):
                raise serializers.ValidationError("잘못된 결제 수단입니다.")
            elif data.get("bank_name") is None:
                raise serializers.ValidationError("은행 이름을 입력해 주세요.")
            elif data.get("bank_account") is None:
                raise serializers.ValidationError("계좌 번호를 입력해 주세요.")
        return data

    class Meta:
        model = PaymentMethod
        fields = "__all__"
        read_only_fields = ["user"]
