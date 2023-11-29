from django.contrib import admin
from django.urls import path

from .views import index, login, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("home/", home, name="home"),
]
