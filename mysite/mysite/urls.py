"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main.views import index, v1, home, create, view
from register.views import register

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("index/", include("main.urls")),
    path("<int:id>", index, name="index"),
    path("v1/", v1, name="View 1!"),
    # path("v1/", include("main.urls")),
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("register/", register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("view/", view, name="view"),
]
