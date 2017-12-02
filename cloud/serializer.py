from rest_framework import serializers

from cloud.models import Door, Profile


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