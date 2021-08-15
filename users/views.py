from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,TemplateView
from django.views import View

from movies.models import Movie, Genre

from .forms import UserRegisterForm, CustomUserChangeForm
from .models import User, UserMovie


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_success_message(self, cleaned_data):
        return f'Welcome {cleaned_data["username"]}! Thank you for joining us.'


class ProfileBaseView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    pass


class ProfileView(ProfileBaseView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Your profile has been updated'

    def get_object(self):
        user = self.request.user
        return User.objects.get(username=user.username)

