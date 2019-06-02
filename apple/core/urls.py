from django.contrib import admin
from django.urls import include, path, re_path

from core.views import HomeView

urlpatterns = [
    re_path(r'^$', view=HomeView.as_view(), name='Home'),
]
