from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from cloud.models import Door, Profile, Log
from cloud.serializer import DoorSerializer, ProfileSerializer, PinSerializer, LogSerializer


class index(APIView):
    def get(self, request):
        door = get_door()
        serializer = DoorSerializer(door, many=False)
        return Response(serializer.data)
    def post(self, request):
        pin = request.data["open"]
        door = get_door()
        door.open = pin
        door.save()
        Log(portaOberta=pin).save()
        serializer = DoorSerializer(door, many=False)
        return Response(serializer.data)




def get_door():
    door = Door.objects.all()
    if not door.exists():
        Door().save()
        door = Door.objects.all()
    return door[0]


class pinV(APIView):
    parser_classes = (JSONParser,)

    def get(self, request, pin=None):
        qs = Profile.objects.all()
        serializer = ProfileSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        pin= request.data["pin"]
        if pin is None:
            Response(status=500)
        user = Profile.objects.filter(pin=pin)
        if not user.exists():
            Log(contrasenyaValida=False).save()
            return Response(status=403)
        else:
            serializer = ProfileSerializer(user[0], many=False)
            Log(contrasenyaValida=True, usuari=user[0]).save()
            return Response(serializer.data)


class logV(generics.ListAPIView):
    serializer_class = LogSerializer
    queryset = Log.objects.all()