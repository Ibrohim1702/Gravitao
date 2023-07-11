from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("clients/", clients, name="clients"),
    path("services/", services, name="services"),
    path("projects/", projects, name="projects"),
]