from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from cloud.models import Door, Profile
from cloud.serializer import DoorSerializer, ProfileSerializer, PinSerializer


class index(APIView):
    def get(self, request):
        door = get_door()
        serializer = DoorSerializer(door, many=False)
        return Response(serializer.data)


def get_door():
    door = Door.objects.all()
    if not door.exists():
        Door().save()
        door = Door.objects.all()
    return door[0]


class pin(APIView):
    def get(self, request):
        qs = Profile.objects.all()
        serializer = ProfileSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PinSerializer(data=data)
        if serializer.is_valid():
            pin = serializer.data["pin"]
            user = Profile.objects.filter(pin=pin)
            if not user.exists():
                JsonResponse(serializer.data, status=403)



        return JsonResponse(serializer.errors, status=400)



