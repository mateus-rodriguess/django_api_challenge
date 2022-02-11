from django.db.models.base import Model
from apps.account.models import User
from rest_framework import serializers
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response


class AccountCreateSerializers(serializers.ModelSerializer):
    "User create"
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