from apps.account.models import User
from rest_framework import serializers


class AccountCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", 'email', "password"]
    
    def create(self, validated_data):
        return super().create(validated_data)


class AccountUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["password", 'email']

    def update(self, instance, validated_data):        
        return super().update(instance, validated_data)