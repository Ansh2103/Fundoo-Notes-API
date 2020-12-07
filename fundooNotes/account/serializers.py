from rest_framework import serializers

from .models import Account

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('id','first_name', 'last_name' ,'userName', 'email' , 'password','date_joined','last_login')