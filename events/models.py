from django.conf import settings
from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва події')
    description = models.TextField(blank=True, verbose_name='Опис')
    date = models.DateTimeField(verbose_name='Дата та час')
    location = models.CharField(max_length=200, blank=True, verbose_name='Місце')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

    def __str__(self):
        return f'{self.title} ({self.date:%d.%m.%Y})'

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})
