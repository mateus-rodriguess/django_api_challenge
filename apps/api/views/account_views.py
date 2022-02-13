from apps.api.serializers import account_serializers
from apps.account.models import User
from rest_framework import generics
from rest_framework.response import Response

class AccountCreateView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = account_serializers.AccountCreateSerializers
    
    
class AccountUpdateView(generics.UpdateAPIView):
    queryset =  User.objects.all()
    serializer_class = account_serializers.AccountUpdateSerializers