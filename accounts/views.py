from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm  # Assuming this is correct for your signup view
from django.views.generic import CreateView

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  # Adjust according to your URL configuration

class LoginView(AuthLoginView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")  # Redirect to home or other appropriate URL after login
