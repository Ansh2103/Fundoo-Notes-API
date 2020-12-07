from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserDetailSerializer
from .models import Account
from rest_framework.permissions import IsAuthenticated
# views

class AccountView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Account.objects.all()
    serializer_class = UserDetailSerializer