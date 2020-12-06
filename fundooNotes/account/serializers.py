from rest_framework import serializers

from .models import UserDetail

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('id','first_name', 'last_name' ,'userName', 'email' , 'password' , 'created')