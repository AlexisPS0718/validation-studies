from django.urls import path
from students import views

urlpatterns = [
  path("", views.StudentListView.as_view(), name="students"),
  path("new/", views.StudentCreateView.as_view(), name="new"),
]
