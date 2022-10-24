from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from projects.views import list_projects

urlpatterns = [path("", list_projects, name="list_projects")]
