from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#Account Serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


#EXAMPLE of creating own post request that arent generic
class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'firstname', 'lastname', 'email')

#Delete account serializer
class DeleteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']