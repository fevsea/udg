from rest_framework import serializers

from cloud.models import Door, Profile, Log


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = ("open",)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Profile
        fields = ("pin", "username")

class PinSerializer(serializers.Serializer):
    pin = serializers.CharField(required=True)

class LogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='get_username')
    descripcio = serializers.CharField(source='__str__')

    class Meta:
        model = Log
        fields = ("id", "datetime", "portaOberta", "contrasenyaValida", "username", "descripcio")