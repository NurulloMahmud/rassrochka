from rest_framework import serializers
from .models import CustomUser, Item


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'is_active']

class ItemViewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = '__all__'
    
    def get_user(self, obj):
        return obj.user.username

class ItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'