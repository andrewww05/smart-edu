from django.urls import path, include
from .controller import PublicController

_publicController = PublicController()

urlpatterns = [
    path("", _publicController.home, name="home"),
    path("faq/", _publicController.faq, name="faq"),
    path("map/", _publicController.map, name="map"),
    path("schedule/", include("apps.schedule.urls")),
]