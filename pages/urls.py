from django.urls import path
from pages import views

urlpatterns = [
  path("", views.HomePageView.as_view(), name="home"),
  path("welcome/", views.WelcomePageView.as_view(), name="index"),
  path("send-mail/", views.ContactPageView.as_view(), name="email"),
]
