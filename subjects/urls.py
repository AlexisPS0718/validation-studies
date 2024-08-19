from django.urls import path
from subjects import views

urlpatterns = [
  path("", views.SubjectListView.as_view(), name="classes"),
  path("new/", views.SubjectCreateView.as_view(), name="new-class"),
  path("<int:pk>/edit/", views.SubjectUpdateView.as_view(), name="edit-class"),
  path("<int:pk>/delete/", views.SubjectDeleteView.as_view(), name="delete-class"),
]
