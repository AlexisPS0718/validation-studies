from django.urls import path
from students import views

urlpatterns = [
  path("", views.StudentListView.as_view(), name="students"),
  path("new/", views.StudentCreateView.as_view(), name="new-student"),
  path("<int:pk>/edit/", views.StudentUpdateView.as_view(), name="edit-student"),
  path("<int:pk>/delete/", views.StudentDeleteView.as_view(), name="delete-student"),
  path('ajax/load-careers/', views.load_careers, name='ajax_load_careers'),
  path("<int:pk>/new-request/", views.RequestCreateView.as_view(), name="new-request"),
  path('ajax/load-request-careers/', views.load_request_careers, name='ajax_load_request_careers'),
  path("<int:pk>/edit-request/", views.RequestUpdateView.as_view(), name="edit-request"),
  path("<int:pk>/delete-request/", views.RequestDeleteView.as_view(), name="delete-request"),
]
