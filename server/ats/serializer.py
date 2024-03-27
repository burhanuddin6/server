from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    "Users serializer"
    class Meta:
        model = Users
        fields = '__all__'


