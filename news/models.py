from django.conf import settings
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Зміст')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Зображення')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'pk': self.pk})
