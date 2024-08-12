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
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Institute, Career

class InstituteListView(LoginRequiredMixin, ListView):
  template_name = "institutes/institutes.html"
  model = Institute

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["institute_list"] = (
      Institute.objects
      .order_by("name")
    )
    return context

class InstituteCreateView(LoginRequiredMixin, CreateView):
  template_name = "institutes/new.html"
  model = Institute
  fields = ["name", "republic_state"]

class InstituteUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "institutes/edit.html"
  model = Institute
  fields = ["name", "republic_state"]

class InstituteDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "institutes/delete.html"
  model = Institute
  success_url = reverse_lazy("institutes")

class CareerListView(LoginRequiredMixin, ListView):
  template_name = "institutes/careers.html"
  model = Institute

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    institute = get_object_or_404(Institute, pk=pk)
    context["institute"] = institute
    context["careers"] = institute.career_set.all().order_by('name')
    return context

class CareerCreateView(LoginRequiredMixin, CreateView):
  template_name = "institutes/new.html"
  model = Career
  fields = ["institution", "name", "is_engineering"]

class CareerUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "institutes/edit.html"
  model = Career
  fields = ["institution", "name", "is_engineering"]

class CareerDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "institutes/delete-career.html"
  model = Career
  
  def get_success_url(self):
    career = self.get_object()
    institute_id = career.institution.id
    return reverse_lazy("careers", args=[institute_id])
