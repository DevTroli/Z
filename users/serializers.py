from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'avatar', 'bio', 'followers']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_avatar(self, obj):
        return obj.avatar
    
    def create(self, validated_data):
        # Extrai a senha antes de criar o usuário
        password = validated_data.pop('password', None)
        
        if not password:
            raise serializers.ValidationError({"password": "Este campo é obrigatório."})
            
        # Usa create_user para garantir hash correto
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password,
            **{k: v for k, v in validated_data.items() if k not in ['username', 'email']}
        )
        return user   
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['avatar'] = user.avatar
        return token
    
    def validate(self, attrs):
        # Permite login com email ou username
        username = attrs.get('username')
        
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                attrs['username'] = user.username
            except User.DoesNotExist:
                pass  # Mantém o username original para gerar erro depois
        
        # Validação principal
        data = super().validate(attrs)
        
        # Adiciona dados do usuário na resposta
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'avatar': self.user.avatar
        }
        
        return data
