"""
app.chat.routing
----------------

"""

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from app.chat_server import routing as rt

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            rt.websocket_urlpatterns
        )
    ),

})