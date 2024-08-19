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
  Subject,
  Career,
  Institute
)

class SubjectListView(LoginRequiredMixin, ListView):
  template_name = "subjects/classes.html"
  model = Subject

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["subject_list"] = (
      Subject.objects
      .order_by("name")
    )
    return context

class SubjectCreateView(LoginRequiredMixin, CreateView):
  template_name = "subjects/new-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["career_list"] = (
      Career.objects
      .order_by("name")
    )
    return context

  def get_success_url(self):
    return reverse_lazy("classes")

class SubjectUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "subjects/edit-class.html"
  model = Subject
  fields = ["career", "key", "name"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk_subject = self.kwargs.get('pk')
    subject = get_object_or_404(Subject, pk=pk_subject)
    context["main_subject"] = subject
    context["institute_list"] = Institute.objects.order_by("name")
    return context

  def get_success_url(self):
    return reverse_lazy("classes")

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "subjects/delete-class.html"
  model = Subject

  def get_success_url(self):
    return reverse_lazy("classes")
