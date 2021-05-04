from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
