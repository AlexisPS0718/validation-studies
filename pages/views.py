from django.views.generic import (
  TemplateView,
  FormView
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  UserPassesTestMixin
)
from students.models import Student
from .forms import contact_form

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["student_list"] = (
      Student.objects
      .order_by("-created_at")
    )
    return context

class ContactPageView(FormView):
  template_name = 'pages/contact.html'
  form_class = contact_form
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    # Extract cleaned data from form
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']

    # Send the email
    send_mail(
        subject=subject,
        message=message + f"\n\nFrom: {name} <{email}>",
        from_email='no-reply@yourdomain.com',  # Customize your sender email
        recipient_list=['alxpesa@gmail.com'],
        fail_silently=False,
    )

    # Display success message
    messages.success(self.request, 'Your message has been sent successfully.')
    
    return super().form_valid(form)

  def form_invalid(self, form):
    # Display error message
    messages.error(self.request, 'There was an error with your submission. Please check the form and try again.')
    
    return super().form_invalid(form)
