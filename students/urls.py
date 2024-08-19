from django.urls import path
from students import views

urlpatterns = [
  path("", views.StudentListView.as_view(), name="students"),
  path("new/", views.StudentCreateView.as_view(), name="new-student"),
  path("<int:pk>/edit/", views.StudentUpdateView.as_view(), name="edit-student"),
  path("<int:pk>/delete/", views.StudentDeleteView.as_view(), name="delete-student"),
  path('ajax/load-careers/', views.load_careers, name='ajax_load_careers'),
]
