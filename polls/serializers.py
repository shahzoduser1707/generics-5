from rest_framework import serializers
from .models import RoomModel

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ('__all__')