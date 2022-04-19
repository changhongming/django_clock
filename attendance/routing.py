'''from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.SyncConsumer),
    path("ws/test_async" , consumers.ChatConsumer.as_asgi()),
]'''

from django.urls import re_path
from attendance import consumers
websocket_urlpatterns = [
  re_path(r'^ws/attendance/(?P<name>[^/]+)/$', consumers.AttendanceConsumer.as_asgi()),
]