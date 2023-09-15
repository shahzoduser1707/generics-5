from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RoomSerializers
from .models import RoomModel
from rest_framework import generics
# Create your views here.

class GetRoom(generics.ListAPIView):
      queryset = RoomModel.objects.all()
      serializer_class = RoomSerializers

class CreateRoom(generics.CreateAPIView):
      queryset = RoomModel.objects.all()
      serializer_class = RoomSerializers
    
class GetCreateRoom(generics.ListCreateAPIView):
      queryset = RoomModel.objects.all()
      serializer_class = RoomSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = RoomModel.objects.all()
      serializer_class = RoomSerializers