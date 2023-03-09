from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import PaymentMethod
from apps.user.serializers import LoginSerializer, PaymentMethodSerializer, SignUpSerializer
from apps.utils.permissions import IsOwner


# api/users/signup
class SignUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입에 성공했습니다."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# api/users/login
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# api/users/logout
class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"message": "유효하지 않은 토큰입니다"}, status=status.HTTP_400_BAD_REQUEST)


# api/users/<int:user_id>/payment-methods
class PaymentMethodView(generics.ListCreateAPIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        payment_method_type = self.request.query_params.get("type")
        queryset = PaymentMethod.objects.filter(user_id=self.kwargs["user_id"])

        if payment_method_type:
            queryset = queryset.filter(payment_method=payment_method_type)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
