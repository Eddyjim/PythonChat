"""
app.chat_server.views
---------------------
Views for chat_server app
"""
import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })