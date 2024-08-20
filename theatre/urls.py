from rest_framework import routers
from django.urls import path, include

from theatre.views import GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("halls", TheatreHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "theatre"
