from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("login", views.login_view, name = "login"),
    path("", views.index, name = "index"),
    path("logout", views.logout_view, name = "logout"),
    path("register", views.register, name = "register"),
    path("history", views.history, name = "history")
]
