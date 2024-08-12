from django.urls import path
from institutes import views

urlpatterns = [
  path("", views.InstituteListView.as_view(), name="institutes"),
  path("new/", views.InstituteCreateView.as_view(), name="new"),
  path("<int:pk>/edit/", views.InstituteUpdateView.as_view(), name="edit"),
  path("<int:pk>/delete/", views.InstituteDeleteView.as_view(), name="delete"),
  path("<int:pk>/careers/", views.CareerListView.as_view(), name="careers"),
  path("new-career/", views.CareerCreateView.as_view(), name="new-career"),
  path("<int:pk>/edit-career/", views.CareerUpdateView.as_view(), name="edit-career"),
  path("<int:pk>/delete-career/", views.CareerDeleteView.as_view(), name="delete-career"),
]
