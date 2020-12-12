from django.contrib.auth.models import User, Group
from api.models import Account
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.decorators import api_view
from api.serializers import UserSerializer, GroupSerializer, AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/accounts/',
        'Get Specific Account': '/accounts/<str:pk>/',
        'Create': '/create-account/',
        'Update': '/update-account/<str:pk>/',
        'Delete': '/delete-account/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def listAccounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSpecificAccount(request,pk):
    accounts = Account.objects.get(id=pk)
    serializer = AccountSerializer(accounts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAccount(request):
    serializer = AccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateAccount(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(instance=account,data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAccount(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
        
    return Response('Item successfully deleted!')


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

