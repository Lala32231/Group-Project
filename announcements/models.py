from django.conf import settings
from django.db import models
from django.urls import reverse


class Announcement(models.Model):
    class Priority(models.TextChoices):
        NORMAL = 'normal', 'Звичайне'
        IMPORTANT = 'important', 'Важливе'
        URGENT = 'urgent', 'Термінове'

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Зміст')
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.NORMAL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcements:detail', kwargs={'pk': self.pk})
