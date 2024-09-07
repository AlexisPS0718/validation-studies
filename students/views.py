from django.views.generic import (
  TemplateView,
  DetailView,
  ListView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import (
  get_object_or_404,
  render
)
from institutes.models import Career
from equivalences.models import (
  Request,
  Analysis,
  DocAnalysis
)
from .forms import (
  StudentForm,
  RequestForm
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

class RequestCreateView(LoginRequiredMixin, CreateView):
  template_name = "students/new-request.html"
  model = Request
  form_class = RequestForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    return context

def load_request_careers(request):
  institute_id = request.GET.get('to_institute')
  careers = Career.objects.filter(institute_id=institute_id).order_by('name')
  return render(request, 'hr/career_dropdown_list_options.html', {'careers': careers})

class RequestUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "students/edit-request.html"
  model = Request
  form_class = RequestForm

class RequestDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "students/delete-request.html"
  model = Request
  success_url = reverse_lazy("students")

class RequestView(LoginRequiredMixin, TemplateView):
  template_name = "students/request.html"
  model = Student

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    return context

class AnalysisCreateView(LoginRequiredMixin, CreateView):
  template_name = "students/new-adoc.html"
  model = DocAnalysis
  fields = ["student", "analysis", "academy_president", "department_head"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    context["analysis_list"] = (
      Analysis.objects
      .order_by("origin_syllabus")
    )
    return context

class AnalysisDetailView(LoginRequiredMixin, DetailView):
  template_name = "students/adoc.html"
  model = DocAnalysis

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    context["equivalence_list"] = student.analysis.analysis.equivalence_set.all().order_by('origin_subject')
    return context

class AnalysisUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "students/edit-adoc.html"
  model = DocAnalysis
  fields = ["academy_president", "department_head"]

class AnalysisDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "students/delete-adoc.html"
  model = DocAnalysis
  success_url = reverse_lazy("students")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    context["equivalence_list"] = student.analysis.analysis.equivalence_set.all().order_by('origin_subject')
    return context

class DictumDetailView(LoginRequiredMixin, TemplateView):
  template_name = "students/dictum.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)
    context["student"] = student
    context["equivalence_list"] = student.analysis.analysis.equivalence_set.all().order_by('origin_subject')
    return context
