from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'username': {
                'error_messages': {
                    'required': 'El nombre de usuario es requerido',
                    'invalid': 'El nombre de usuario debe ser una cadena de texto válida'
                }
            },
            'email': {
                'error_messages': {
                    'required': 'El email es requerido',
                    'invalid': 'Por favor, introduce un email válido'
                }
            }
        }


class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(error_messages={
        'invalid': 'El email no puede estar vacío',
        'required': 'El email es requerido'
    })
    # last_name = serializers.CharField(max_length=100)
    
    def validate_name(self,value):
        if "Joerl" in value:
            raise serializers.ValidationError("ERROR, No se puede usar este nombre")
        return value
   
    # def validate_last_name(self,value):
    #     print(value)
    
    def validate_email(self,value):
        if not value:
            raise serializers.ValidationError("El email no puede estar vacío")
        return value
    
    def validate(self,data):
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    
