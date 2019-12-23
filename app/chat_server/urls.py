"""
app.chat_server.urls
--------------------
URLs for chat_server app
"""

from django.urls import path

from chat_server import views

urlpatterns = [
    path('', views.index, name='chat_room'),
    path('<str:room_name>/', views.room, name='room'),
]
