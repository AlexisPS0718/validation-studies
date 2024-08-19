from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from institutes.models import (
  Syllabus,
  Subject,
  Career,
  Subject,
  Institute
)

class SyllabusListView(LoginRequiredMixin, ListView):
  template_name = "careers/syllabus.html"
  model = Subject

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk)
    context["career"] = career
    context["subject_list"] = career.subject_set.all().order_by('name')
    return context

class SyllabusCreateView(LoginRequiredMixin, CreateView):
  template_name = "careers/new-syllabus.html"
  model = Syllabus
  fields = ["career", "key", "start_date", "final_date"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk)
    context["career"] = career
    return context

class SyllabusUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "careers/edit-syllabus.html"
  model = Syllabus
  fields = ["key", "start_date", "final_date"]

class SyllabusDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "careers/delete-syllabus.html"
  model = Syllabus

  def get_success_url(self):
    syllabus = self.get_object()
    institute_id = syllabus.career.institute.id
    return reverse_lazy("careers", args=[institute_id])

class SubjectCreateView(LoginRequiredMixin, CreateView):
  template_name = "careers/new-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk)
    institute_id = career.institute.id
    institute = get_object_or_404(Institute, pk=institute_id)
    context["main_career"] = career
    context["career_list"] = institute.career_set.all().order_by('name')
    return context

  def get_success_url(self):
    pk = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk)
    return reverse_lazy("syllabus", args=[career.id])

class SubjectUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "careers/edit-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk_career = self.kwargs.get('pk1')
    pk_subject = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk_career)
    subject = get_object_or_404(Subject, pk=pk_subject)
    institute_id = career.institute.id
    institute = get_object_or_404(Institute, pk=institute_id)
    context["main_career"] = career
    context["main_subject"] = subject
    context["career_list"] = institute.career_set.all().order_by('name')
    return context

  def get_success_url(self):
    pk_career = self.kwargs.get('pk1')
    return reverse_lazy("syllabus", args=[pk_career])

class SubjectAddView(LoginRequiredMixin, UpdateView):
  template_name = "careers/add-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk_career = self.kwargs.get('pk1')
    pk_subject = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk_career)
    subject = get_object_or_404(Subject, pk=pk_subject)
    context["main_career"] = career
    context["main_subject"] = subject
    context["institute_list"] = Institute.objects.order_by("name")
    return context

  def get_success_url(self):
    pk_career = self.kwargs.get('pk1')
    return reverse_lazy("syllabus", args=[pk_career])

class SubjectSubtractView(LoginRequiredMixin, UpdateView):
  template_name = "careers/subtract-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk_career = self.kwargs.get('pk1')
    pk_subject = self.kwargs.get('pk')
    career = get_object_or_404(Career, pk=pk_career)
    subject = get_object_or_404(Subject, pk=pk_subject)
    context["main_career"] = career
    context["main_subject"] = subject
    context["institute_list"] = Institute.objects.order_by("name")
    return context

  def get_success_url(self):
    pk_career = self.kwargs.get('pk1')
    return reverse_lazy("syllabus", args=[pk_career])
