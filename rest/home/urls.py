from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("wether/", views.WetherInfo.as_view(), name="wether"),
]
