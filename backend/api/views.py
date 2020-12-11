from django.contrib.auth.models import User, Group
from api.models import Account
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status, generics
from api.serializers import UserSerializer, GroupSerializer, AccountSerializer, CreateAccountSerializer, DeleteAccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateAccountView(APIView):
    serializer_class = CreateAccountSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            firstname = serializer.data.get('firstname')
            lastname = serializer.data.get('lastname')
            email = serializer.data.get('email')

            account = Account(username=username, firstname=firstname, lastname=lastname, email=email)
            account.save()

            return Response(AccountSerializer(account).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccountView(APIView):
    def delete(self, request, pk):
        print(pk)
        try:
            account = Account.objects.get(id=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        