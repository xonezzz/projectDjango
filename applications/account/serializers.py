from rest_framework import serializers 
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']


    # def validate_email(self, email):
    #     print(email) 

    #     return email 

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs 

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        # TODO: send message
        user.is_active = True 

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(username=email,
                            password=password)
        if not user:
            raise serializers.ValidationError('Неверный email или пароль')
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        min_length=6
    )
    new_password_confrim = serializers.CharField(
        required=True,
        min_length=6
    )

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confrim')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def validate_old_password(self, p):
        request = self.context.get('request')
        user = request.user
        if user.check_password(p):
            raise serializers.ValidationError('Неверный пароль!')
        return p

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()
