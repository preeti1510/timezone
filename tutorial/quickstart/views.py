from django.shortcuts import render
import pytz
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer

from django.utils import timezone
import socket
from datetime import datetime
from dateutil import tz
unlocalisedDatetime = datetime.now()
localisedDatetime = unlocalisedDatetime.astimezone(tz = tz.tzlocal())
print(localisedDatetime)
# from datetime import datetime, timezone
#
# now = datetime.now()
#
# print(now.replace(tzinfo=timezone.utc) - now.astimezone(timezone.utc))
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

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
