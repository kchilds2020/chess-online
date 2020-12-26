from django.contrib.auth.models import Group
from django.db.models import query
from django.db.models.lookups import GreaterThan
from api.models import User, Queue, Match
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import UserSerializer, GroupSerializer, MatchSerializer, QueueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/users/',
        'Get Specific Account': '/users/<str:pk>/',
        'Create': '/create-user/',
        'Update': '/update-user/<str:pk>/',
        'Delete': '/delete-user/<str:pk>/',
        'Get Queue': '/get-queue/',
        'Get Matches': '/get-matches/'
    }
    return Response(api_urls)

@api_view(['GET'])
def listUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listQueue(request):
    queue = Queue.objects.all()
    serializer = QueueSerializer(queue, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listMatches(request):
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSpecificUser(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    data= serializer.data
    del data['password']
    return Response(data)

@api_view(['GET'])
def getMatch(request,pk):
    match = Match.objects.get(id=pk)
    serializer = MatchSerializer(match, many=False)
    data= serializer.data
    return Response(data)

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
    if 'username' in serializer.data:
        password = request.data['password']
        if check_password(password, serializer.data['password']):
            data={}
            data['id'] = serializer.data['id']
            data['username'] = serializer.data['username']
            data['firstname'] = serializer.data['firstname']
            data['lastname'] = serializer.data['lastname']
            data['email'] = serializer.data['email']
            data['password'] = serializer.data['password']
            data['token'] = Token.objects.get(user=serializer.data['id']).key
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response('password is incorrect', status=status.HTTP_206_PARTIAL_CONTENT)
    else:
        return Response('incorrect username', status=status.HTTP_206_PARTIAL_CONTENT)

@api_view(['POST'])
def addToQueue(request):

    #validate data
    serializer = QueueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def addToMatch(request):
    #validate data
    serializer = MatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def findMatch(request):
    #validate data
    queue = Queue.objects.all()
    #see if anyone is in the queue
    if queue.count() == 0:
        #add to queue if no is in the queue
        queue_serializer = QueueSerializer(data=request.data)
        if queue_serializer.is_valid():
            queue_serializer.save()
            return Response('added to queue')
        else:
            return Response(queue_serializer.errors)
    else:
        #create a match with first person in queue
        queue_serializer = QueueSerializer(queue, many=True)
        user_in_queue = queue_serializer.data[0]
        data = {}
        data['black'] = request.data['username']
        data['white'] = user_in_queue['username']
        
        match_serializer = MatchSerializer(data = data)
        #create match and delete user from queue

        if match_serializer.is_valid():
            match_serializer.save()
            #update users active_games field
            black_username = User.objects.get(username=data['black'])
            black_user = UserSerializer(black_username)

            black_user_data = {}
            black_user_data['id']=black_user['id'].value
            black_user_data['username'] = black_user['username'].value
            black_user_data['email'] = black_user['email'].value
            black_user_data['firstname'] = black_user['firstname'].value
            black_user_data['lastname'] = black_user['lastname'].value
            black_user_data['active_games'] = black_user['active_games'].value
            black_user_data['password'] = black_user['password'].value

            print("USER DATA")
            print(black_user_data)
            if 'games' in black_user_data['active_games']:
                games = black_user_data['active_games']['games']
                games.append(match_serializer.data)
            else:
                black_user_data['active_games']['games'] = []
                black_user_data['active_games']['games'].append(match_serializer.data)

            black_serializer = UserSerializer(instance=black_username,data=black_user_data)
            if black_serializer.is_valid():
                black_serializer.save()
            else:
                print(black_serializer.errors)

            white_username = User.objects.get(username=data['white'])
            white_user = UserSerializer(white_username)

            white_user_data = {}
            white_user_data['id']=white_user['id'].value
            white_user_data['username'] = white_user['username'].value
            white_user_data['email'] = white_user['email'].value
            white_user_data['firstname'] = white_user['firstname'].value
            white_user_data['lastname'] = white_user['lastname'].value
            white_user_data['active_games'] = white_user['active_games'].value
            white_user_data['password'] = white_user['password'].value

            if 'games' in white_user_data['active_games']:
                games = white_user_data['active_games']['games']
                games.append(match_serializer.data)
            else:
                white_user_data['active_games']['games'] = []
                white_user_data['active_games']['games'].append(match_serializer.data)

            white_serializer = UserSerializer(instance=white_username,data=white_user_data)
            if white_serializer.is_valid():
                white_serializer.save()
            else:
                print(white_serializer.errors)
                

            user_to_delete = Queue.objects.get(id=user_in_queue['id'])
            user_to_delete.delete()
            return Response(match_serializer.data)
        else:
            return Response(match_serializer.errors)



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
