__author__ = 'butlernc'

from rest_framework import serializers
from Users.models import User, Location, GPSRequest

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=55)
    password = serializers.CharField(max_length=55)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.username)

class LocationSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=55)
    long = serializers.DecimalField(max_digits=25, decimal_places=25)
    lat = serializers.DecimalField(max_digits=25, decimal_places=25)

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.long = validated_data.get('long', instance.long)
        instance.lat = validated_data.get('lat', instance.lat)


class GPSRequestSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username_requester = serializers.CharField(max_length=55)
    username_requested = serializers.CharField(max_length=55)

    def create(self, validated_data):
        return GPSRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username_requester = validated_data.get('username_requester', instance.username_requester)
        instance.username_requested = validated_data.get('username_requested', instance.username_requested)
