from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializers import UserDetailSerializer
from .models import UserDetail

class AccountView(ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer