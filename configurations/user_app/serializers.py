from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()



class NewUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model=UserModel
        fields=["email","last_name","first_name","pk","nickname", "username", "birth_date", "profile_picture", "name_profile_picture"]


class NewRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField()
    birth_date = serializers.DateField()

    def validate_email(self, value):
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Почта уже используется")
        return value
    
    

    def custom_signup(self, request, user):
        user.nickname = request.data['nickname']
        user.birth_date = request.data['birth_date']
        user.save()

class NewLoginSerializer(LoginSerializer):
    pass


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'username', 'nickname', 'email', 'birth_date', 'profile_picture', 'is_superuser']



class UserListUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'username', 'nickname', 'email', 'birth_date']





class ProfilePictureUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['profile_picture']

    def update(self, instance, validated_data):
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance












class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=1)

    class Meta:
        fields = ("password",)

    def validate(self, data):
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = UserModel.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data




class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    def validate(self, data):
        return data