from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Users.models import User, Location
from Users.serializers import UserSerializer, LocationSerializer, GPSRequestSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET', 'POST'])
@csrf_exempt
def user_list(request):

    if request.method == 'GET':

        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        locations = Location.objects.all()
        locationSerializer = LocationSerializer(locations, many=True)

        return Response(locationSerializer.data)

    elif request.method == 'POST':
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def new_user(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
def receive_gps(request):
    if request.method == 'POST':
        gps_request_serializer = GPSRequestSerializer(data=request.data)
        if gps_request_serializer.is_valid():
            gps_request_serializer.save()
            # each request will send a username for now, later on they will send a c2a tag too
            # step one: create a data object that will the two user names
            # step two: create our C2M object that will send the the username to the correct user
            # that they want gps coords from.
            return Response(gps_request_serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
def user_detail(request, username):
    try:
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
