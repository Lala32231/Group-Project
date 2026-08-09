from django.contrib.auth.mixins import UserPassesTestMixin


class ModeratorRequiredMixin(UserPassesTestMixin):
    """Дозволяє доступ модераторам та адміністраторам."""
    raise_exception = False
    login_url = 'accounts:login'

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_moderator or user.is_admin_role)


class AdminRequiredMixin(UserPassesTestMixin):
    """Дозволяє доступ лише адміністраторам (викладач/керівник + призначені)."""
    raise_exception = False
    login_url = 'accounts:login'

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_admin_role
