"""Votify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from VoteApi.consumers import Con
from VoteApi import views

urlpatterns = [
    path('ws/vote_count', Con.as_asgi()),
     path("login",views.login),
     path("signup",views.create_account),
     path("candidate/add",views.add_candidate),
     path("candidate/get",views.Get_Candidates.as_view()),
     path("vote/cast",views.cast_vote)

]
