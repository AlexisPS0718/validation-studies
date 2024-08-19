from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from institutes.models import Career
from .forms import StudentForm
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
  form_class = StudentForm

class StudentUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "students/edit.html"
  model = Student
  form_class = StudentForm

def load_careers(request):
  institute_id = request.GET.get('institute')
  careers = Career.objects.filter(institute_id=institute_id).order_by('name')
  return render(request, 'hr/career_dropdown_list_options.html', {'careers': careers})

class StudentDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "students/delete.html"
  model = Student
  success_url = reverse_lazy("students")
