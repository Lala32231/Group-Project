from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .forms import RegisterForm, ProfileEditForm, RoleChangeForm
from .models import User
from .permissions import AdminRequiredMixin


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Реєстрація успішна! Ласкаво просимо на портал групи.')
        return response


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'core:home'


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk:
            return User.objects.get(pk=pk)
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профіль оновлено.')
        return super().form_valid(form)


class UserListView(AdminRequiredMixin, ListView):
    """Список користувачів для адміністратора — управління ролями."""
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    paginate_by = 20


class RoleChangeView(AdminRequiredMixin, UpdateView):
    model = User
    form_class = RoleChangeForm
    template_name = 'accounts/role_change.html'
    success_url = reverse_lazy('accounts:user_list')

    def form_valid(self, form):
        messages.success(self.request, f'Роль користувача {self.object.username} оновлено.')
        return super().form_valid(form)
