from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about_me, name = 'about'),
    path("contact/", views.contact, name = "contact"),
    path("portfolio/", views.portfolio, name = 'portfolio'),
    path("blog/", views.blog, name = "blog"),
]