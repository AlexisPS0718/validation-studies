from django.urls import path
from institutes.views import (
  CareerUpdateView, 
  CareerDeleteView
)
from careers import views

urlpatterns = [
  path("<int:pk>/edit/", CareerUpdateView.as_view(), name="edit-career"),
  path("<int:pk>/delete/", CareerDeleteView.as_view(), name="delete-career"),
  path("<int:pk>/syllabus/", views.SyllabusListView.as_view(), name="syllabus"),
  path("<int:pk>/new-syllabus/", views.SyllabusCreateView.as_view(), name="new-syllabus"),
  path("<int:pk>/edit-syllabus/", views.SyllabusUpdateView.as_view(), name="edit-syllabus"),
  path("<int:pk>/delete-syllabus/", views.SyllabusDeleteView.as_view(), name="delete-syllabus"),
  path("<int:pk>/new-class/", views.SubjectCreateView.as_view(), name="new-class"),
  path("<int:pk1>/edit-class/<int:pk>/", views.SubjectUpdateView.as_view(), name="edit-class"),
  path("<int:pk1>/add-class/<int:pk>/", views.SubjectAddView.as_view(), name="add-class"),
  path("<int:pk1>/subtract-class/<int:pk>/", views.SubjectSubtractView.as_view(), name="subtract-class"),
]
