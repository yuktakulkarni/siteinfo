from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("login", views.login),
    path("calc", views.calc),
    path("contact", views.contact),
    path("faq", views.faq),
    path("news", views.news),
    path("subscribe", views.subscribe),
    path("Bitcoin", views.Bitocin),
    path("Ethereum", views.Ethereum),
    path("Cardano", views.Cardano),
    path("XRP", views.XRP),
    path("Dogecoin", views.Dogecoin),
]
