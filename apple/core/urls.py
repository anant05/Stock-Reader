from django.contrib import admin
from django.urls import include, path, re_path

from core.views import HomeView, AboutView

urlpatterns = [
    re_path(r'^$', view=HomeView.as_view(), name='home'),
    re_path(r'about/', view=AboutView.as_view(), name='about'),
]
