from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import Role

class SignUpView(CreateView):
  template_name = "registration/signup.html"
  form_class = CustomUserCreationForm
  success_url = reverse_lazy("login")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["role_list"] = Role.objects.order_by('name')
    return context
