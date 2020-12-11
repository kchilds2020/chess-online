from django.contrib.auth.models import User, Group
from api.models import Account
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



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


""" class CreateMatchView(APIView):
    serializer_class = CreateMatchSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            value = serializer.data.value
            queryset = Match.objects.filter(id=id)
            if queryset.exists():
                match = queryset[0]
                match.value = value
                match.save(update_fields=['value'])
            else:
                match = Match(value = value)
                match.save()

            return Response(MatchSerializer(match.data), status=status.HTTP_200_OK) """