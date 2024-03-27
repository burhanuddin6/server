# from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializer import UsersSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer


