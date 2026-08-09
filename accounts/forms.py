from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label="Ім'я")
    last_name = forms.CharField(required=True, label='Прізвище')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'group_name', 'password1', 'password2']
        labels = {
            'username': "Логін",
            'group_name': 'Група',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # Роль за замовчуванням — "Користувач", підвищити можуть лише адміни через адмінку/панель
        user.role = User.Role.USER
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'group_name', 'bio', 'avatar']
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
            'email': 'Email',
            'group_name': 'Група',
            'bio': 'Про себе',
            'avatar': 'Аватар',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class RoleChangeForm(forms.ModelForm):
    """Форма для адміністратора — змінити роль користувача."""
    class Meta:
        model = User
        fields = ['role']
        labels = {'role': 'Роль'}
