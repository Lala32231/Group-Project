from django.conf import settings
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False, verbose_name='Закрита')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Тема форуму'
        verbose_name_plural = 'Теми форуму'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:topic_detail', kwargs={'pk': self.pk})

    @property
    def posts_count(self):
        return self.posts.count()


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Повідомлення')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'

    def __str__(self):
        return f'{self.author}: {self.content[:30]}'
