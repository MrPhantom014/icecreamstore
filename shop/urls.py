from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index,name="index"),
    path("about/", views.about,name="about"),
    path("products/", views.products,name="products"),
    path("contact/", views.contact,name="contact"),
    path("login/", views.loginUser,name="loginUser"),
    path("logout/", views.logoutUser,name="logoutUser")
]