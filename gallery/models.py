from django.conf import settings
from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва альбому')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбоми'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'pk': self.pk})


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/', verbose_name='Фото')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Підпис')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.caption or f'Фото #{self.pk}'
