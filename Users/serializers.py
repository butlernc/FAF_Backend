__author__ = 'butlernc'

from rest_framework import serializers
from Users.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=55)
    password = serializers.CharField(max_length=55)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.username)
