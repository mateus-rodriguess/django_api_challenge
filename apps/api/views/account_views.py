from apps.api.serializers import account_serializers
from apps.account.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class AccountCreateView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset =  User.objects.all()
    serializer_class = account_serializers.AccountCreateSerializers


class AccountUpdateView(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset =  User.objects.all()
    serializer_class = account_serializers.AccountUpdateSerializers