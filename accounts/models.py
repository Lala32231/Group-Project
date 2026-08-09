from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомна модель користувача з ролями доступу.
    Ролі:
      - user (Користувач) — базова роль за замовчуванням
      - moderator (Модератор) — може модерувати контент (новини, форум, оголошення)
      - admin (Адміністратор) — повний доступ (викладач / керівник проекту)
    """

    class Role(models.TextChoices):
        USER = 'user', 'Користувач'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Адміністратор'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Роль',
    )
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True, verbose_name='Аватар'
    )
    bio = models.TextField(blank=True, verbose_name='Про себе')
    group_name = models.CharField(
        max_length=100, blank=True, verbose_name='Група'
    )

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR or self.is_admin_role

    @property
    def is_admin_role(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    def __str__(self):
        return self.get_full_name() or self.username
