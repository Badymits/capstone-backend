from django.urls import path

from . import views

urlpatterns = [
    path('create-lobby/', views.gameLobby, name='create-lobby'),
    path('get-lobby/<str:lobby_code>/', views.LobbyView.as_view(), name='get-lobby'),
    path('get-lobby-list/', views.LobbyRoomList.as_view(), name='get-lobby-list'),
]


