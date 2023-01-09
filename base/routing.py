from django.urls import path
from . import consumers
# import room.routing

websocket_urlpatterns = [
    path('chat/', consumers.ChatConsumer.as_asgi()),
]
