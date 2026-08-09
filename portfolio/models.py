from django.conf import settings
from django.db import models
from django.urls import reverse


class PortfolioItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=200, verbose_name='Назва роботи')
    description = models.TextField(blank=True, verbose_name='Опис')
    file = models.FileField(upload_to='portfolio/', blank=True, null=True, verbose_name='Файл/матеріал')
    link = models.URLField(blank=True, verbose_name='Посилання')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Робота портфоліо'
        verbose_name_plural = 'Портфоліо'

    def __str__(self):
        return f'{self.title} ({self.owner})'

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'pk': self.pk})
