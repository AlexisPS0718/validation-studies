from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import (
  Analysis,
  Career,
  Equivalence,
  Syllabus
)

class AnalysisListView(LoginRequiredMixin, ListView):
  template_name = "equivalences/analysis.html"
  model = Analysis

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["analysis_list"] = (
      Analysis.objects
      .order_by("origin_syllabus")
    )
    return context

class AnalysisCreateView(LoginRequiredMixin, CreateView):
  template_name = "equivalences/new-analysis.html"
  model = Analysis
  fields = ["origin_syllabus", "receiver_syllabus"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["syllabus_list"] = (
      Syllabus.objects
      .order_by("career")
    )
    return context

class AnalysisUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "equivalences/edit-analysis.html"
  model = Analysis
  fields = ["origin_syllabus", "receiver_syllabus"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    analysis = get_object_or_404(Analysis, pk=pk)
    context["analysis"] = analysis
    context["syllabus_list"] = (
      Syllabus.objects
      .order_by("career")
    )
    return context

class AnalysisDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "equivalences/delete-analysis.html"
  model = Analysis
  success_url = reverse_lazy("analysis")

class EquivalenceListView(LoginRequiredMixin, ListView):
  template_name = "equivalences/equivalences.html"
  model = Equivalence

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    analysis = get_object_or_404(Analysis, pk=pk)
    origin_career_id = analysis.origin_syllabus.career.id
    origin_career = get_object_or_404(Career, pk=origin_career_id)
    context["analysis"] = analysis
    context["origin_career"] = origin_career
    context["origin_subject_list"] = origin_career.subject_set.all().order_by('name')
    context["equivalence_list"] = analysis.equivalence_set.all().order_by('origin_subject')
    context["equivalence_origin_list"] = analysis.equivalence_set.all().values_list('origin_subject', flat=True)
    return context

class EquivalenceCreateView(LoginRequiredMixin, CreateView):
  template_name = "equivalences/new-equivalence.html"
  model = Equivalence
  fields = ["analysis", "origin_subject", "receiver_subject", "percentage"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    analysis = get_object_or_404(Analysis, pk=pk)
    origin_career_id = analysis.origin_syllabus.career.id
    receiver_career_id = analysis.receiver_syllabus.career.id
    origin_career = get_object_or_404(Career, pk=origin_career_id)
    receiver_career = get_object_or_404(Career, pk=receiver_career_id)
    context["analysis"] = analysis
    context["origin_career"] = origin_career
    context["receiver_career"] = receiver_career
    context["origin_subject_list"] = origin_career.subject_set.all().order_by('name')
    context["receiver_subject_list"] = receiver_career.subject_set.all().order_by('name')
    return context

  def get_success_url(self):
    pk_analysis = self.kwargs.get('pk')
    return reverse_lazy("equivalences", args=[pk_analysis])

class EquivalenceUpdateView(LoginRequiredMixin, UpdateView):
  template_name = "equivalences/edit-equivalence.html"
  model = Equivalence
  fields = ["analysis", "origin_subject", "receiver_subject", "percentage"]

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs.get('pk')
    pk1 = self.kwargs.get('pk1')
    analysis = get_object_or_404(Analysis, pk=pk1)
    equivalence = get_object_or_404(Equivalence, pk=pk)
    origin_career_id = analysis.origin_syllabus.career.id
    receiver_career_id = analysis.receiver_syllabus.career.id
    origin_career = get_object_or_404(Career, pk=origin_career_id)
    receiver_career = get_object_or_404(Career, pk=receiver_career_id)
    context["analysis"] = analysis
    context["equivalence"] = equivalence
    context["origin_career"] = origin_career
    context["receiver_career"] = receiver_career
    context["origin_subject_list"] = origin_career.subject_set.all().order_by('name')
    context["receiver_subject_list"] = receiver_career.subject_set.all().order_by('name')
    return context

  def get_success_url(self):
    pk_analysis = self.kwargs.get('pk1')
    return reverse_lazy("equivalences", args=[pk_analysis])

class EquivalenceDeleteView(LoginRequiredMixin, DeleteView):
  template_name = "equivalences/delete-equivalence.html"
  model = Equivalence

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk_analysis = self.kwargs.get('pk1')
    analysis = get_object_or_404(Analysis, pk=pk_analysis)
    context["analysis"] = analysis
    return context

  def get_success_url(self):
    pk_analysis = self.kwargs.get('pk1')
    return reverse_lazy("equivalences", args=[pk_analysis])
