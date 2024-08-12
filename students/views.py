from django.views.generic import (
  TemplateView,
  ListView,
  CreateView,
  DetailView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  UserPassesTestMixin
)
from .models import Student

class StudentListView(LoginRequiredMixin, ListView):
  template_name = "students/students.html"
  model = Student

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["students_list"] = (
      Student.objects
      .order_by("first_name")
    )
    return context

class StudentCreateView(LoginRequiredMixin, CreateView):
  template_name = "students/new.html"
  model = Student
  fields = ["institution", "career", "first_name", "paternal_surname", "maternal_surname", "street_and_number", "neighborhood", "zip_code", "municipality", "city", "state", "nationality", "sex", "level", "area"]
