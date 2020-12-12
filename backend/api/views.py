from django.contrib.auth.models import User, Group
from api.models import Account
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.decorators import api_view
from api.serializers import UserSerializer, GroupSerializer, AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

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
    if 'user' in request.session:
        print(request.session['user'])

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
        username = serializer.data['username']
        firstname = serializer.data['firstname']
        lastname = serializer.data['lastname']
        email = serializer.data['email']
        password = make_password(serializer.data['password'])
        account = Account(username=username, firstname=firstname, lastname=lastname, email=email, password=password)
        account.save()
        request.session['user'] = serializer.data
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

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

#check if user has a session
@api_view(['GET'])
def checkSession(request):
    if 'user' in request.session:
        return Response(request.session['user'])
    else:
        return Response('user not found')

#login user
@api_view(['GET'])
def checkSession(request):
    if 'user' in request.session:
        return Response(request.session['user'])
    else:
        return Response('user not found')

#delete user
@api_view(['GET'])
def logout(request):
    del request.session['user']
    return Response('user logged out')


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

