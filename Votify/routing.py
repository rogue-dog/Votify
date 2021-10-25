from channels.routing import ProtocolTypeRouter,URLRouter
from . import urls

application = ProtocolTypeRouter({
    "websocket" : URLRouter(
        urls.urlpatterns
    ),
    
})