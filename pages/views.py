from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  UserPassesTestMixin
)

class HomePageView(TemplateView):
  template_name = "pages/home.html"

  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      user_role = self.request.user.role
      if user_role.name == "Administrator":
          return redirect('index')
    return super(HomePageView, self).dispatch(request, *args, **kwargs)

class WelcomePageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
  template_name = "pages/index.html"

  def test_func(self):
    user_role = self.request.user.role
    return user_role.name == "Administrator"
