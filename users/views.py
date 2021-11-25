from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import SignupForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class SignupPageView(SuccessMessageMixin,CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = "Signup Success"