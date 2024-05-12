"""
URL configuration for DjangoSKJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Frontend.views import index, summonerView
from RiotAPIHandler.views import summonerProfile, summonerMatchHistory, MatchDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summoner/', summonerView, name='summoner'),
    #path('summoner/save', save_summoner, name='save_summoner'),  # Handles the POST request from the form
    path('summoner/<str:server>/<str:summonername>/', summonerProfile, name='SummonerProfile'),
    path('summoner/<str:server>/<str:summonername>/matchhistory', summonerMatchHistory, name='SummonerMatchHistory'),
    path('matchdetail/<str:server>/<str:matchid>', MatchDetail, name='MatchDetail'),
    path('', index, name='home'),
]
