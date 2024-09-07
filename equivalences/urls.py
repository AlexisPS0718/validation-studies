from django.urls import path
from equivalences import views

urlpatterns = [
  path("", views.AnalysisListView.as_view(), name="analysis"),
  path("new/", views.AnalysisCreateView.as_view(), name="new-analysis"),
  path("<int:pk>/edit/", views.AnalysisUpdateView.as_view(), name="edit-analysis"),
  path("<int:pk>/delete/", views.AnalysisDeleteView.as_view(), name="delete-analysis"),
  path("<int:pk>/equivalences/", views.EquivalenceListView.as_view(), name="equivalences"),
  path("<int:pk>/new-equivalence/", views.EquivalenceCreateView.as_view(), name="new-equivalence"),
  path("<int:pk1>/edit-equivalence/<int:pk>/", views.EquivalenceUpdateView.as_view(), name="edit-equivalence"),
  path("<int:pk1>/delete-equivalence/<int:pk>/", views.EquivalenceDeleteView.as_view(), name="delete-equivalence"),
]
