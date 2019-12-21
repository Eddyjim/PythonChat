"""
app.chat_server.urls
--------------------
URLs for chat_server app
"""

from django.urls import path

from app.chat_server import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
