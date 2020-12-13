from django.contrib.auth.models import Group
from api.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.decorators import api_view
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/users/',
        'Get Specific Account': '/accounts/<str:pk>/',
        'Create': '/create-account/',
        'Update': '/update-account/<str:pk>/',
        'Delete': '/delete-account/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def listUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSpecificUser(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    #encrypt password
    enc_password = make_password(request.data['password'])
    request.data['password'] = enc_password

    #validate data
    serializer = UserSerializer(data=request.data)

    data={}
    if serializer.is_valid():
        account = serializer.save()
        data['username'] = serializer.data['username']
        data['firstname'] = serializer.data['firstname']
        data['lastname'] = serializer.data['lastname']
        data['email'] = serializer.data['email']
        data['password'] = serializer.data['password']
        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user,data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
        
    return Response('Item successfully deleted!')

#login user
@api_view(['POST'])
def login(request):
    #verify username and password
    user = User.objects.get(username=request.data['username'])
    
    serializer = UserSerializer(user, many=False)
    print(serializer.data)
    if 'username' in serializer.data:
        password = request.data['password']
        if check_password(password, serializer.data['password']):
            data={}
            data['username'] = serializer.data['username']
            data['firstname'] = serializer.data['firstname']
            data['lastname'] = serializer.data['lastname']
            data['email'] = serializer.data['email']
            data['password'] = serializer.data['password']
            data['token'] = Token.objects.get(user=serializer.data['id']).key
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response('password is incorrect')
    else:
        return Response('incorrect username')


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

