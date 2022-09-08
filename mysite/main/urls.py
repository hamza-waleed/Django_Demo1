from django.urls import path
from . import views

urlpatters = [
    path("index/", views.index, name="index"),
    path("v1/", views.v1, name="View 1"),
]
