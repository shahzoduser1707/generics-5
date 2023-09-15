from django.urls import path
from .views import GetRoom,CreateRoom,GetCreateRoom,DetailUpdateDestroy

urlpatterns = [
    path('getRoom/',GetRoom.as_view()),
    path('createRoom/',CreateRoom.as_view()),
    path('getcreateRoom/',GetCreateRoom.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]