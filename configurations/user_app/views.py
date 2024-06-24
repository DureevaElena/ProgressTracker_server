from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from .models import PasswordResetData
from .serializers import ProfilePictureUploadSerializer, UserListSerializer,EmailSerializer, ResetPasswordSerializer, UserListUpdateSerializer
from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status
from django.views.generic import DetailView

UserModel = get_user_model()

class ProfilePictureUploadView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = ProfilePictureUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


    
class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer




class UserDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserListUpdateSerializer
    queryset = UserModel.objects.all()
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class PasswordReset(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def get(self, request):
        return Response({"message": "Provide your email to reset password"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = UserModel.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)

            password_reset_data = PasswordResetData.objects.create(
                encoded_pk=encoded_pk,
                token=token,
            )

            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            return Response(
                {"encoded_pk": encoded_pk, "token": token},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST,)


class ResetPasswordAPI(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def patch(self, request, encoded_pk, token):
        serializer = self.serializer_class(
            data=request.data, context={"encoded_pk": encoded_pk, "token": token}
        )
        serializer.is_valid(raise_exception=True)

        # Получаем данные из модели PasswordResetData
        password_reset_data = PasswordResetData.objects.filter(
            encoded_pk=encoded_pk, token=token
        ).first()

        if not password_reset_data:
            return Response(
                {"message": "Invalid encoded_pk or token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Далее ваша логика для сброса пароля
        # В serializer.validated_data['password'] будет новый пароль

        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
