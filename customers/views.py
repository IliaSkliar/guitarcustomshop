from django.urls import reverse_lazy
from django.views import generic

from customers.forms import CustomUserChangeForm
from customers.models import CustomUser
from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Profile(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'profile.html'
    queryset = CustomUser.objects.all()

    def get_object(self, queryset=None):
        return self.request.user
