from django.contrib import admin
from django.urls import path, include
from user.views import *
app_name = "user"
urlpatterns = [
    path("user/", login_view,name="user"),
]
