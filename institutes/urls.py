from django.urls import path
from institutes import views

urlpatterns = [
  path("", views.InstituteListView.as_view(), name="institutes"),
  path("new/", views.InstituteCreateView.as_view(), name="new-institute"),
  path("<int:pk>/edit/", views.InstituteUpdateView.as_view(), name="edit-institute"),
  path("<int:pk>/delete/", views.InstituteDeleteView.as_view(), name="delete-institute"),
  path("<int:pk>/careers/", views.CareerListView.as_view(), name="careers"),
  path("<int:pk>/new-career/", views.CareerCreateView.as_view(), name="new-career"),
]
