'''from channels.routing import ProtocolTypeRouter,URLRouter
import os
from channels.auth import AuthMiddlewareStack
import appname.routing
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # (your routes here)
    'http' : django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            appname.routing.websocket_urlpatterns
        )
    )
})'''