from django.conf import settings
from django.db import models
from django.urls import reverse


class Poll(models.Model):
    question = models.CharField(max_length=255, verbose_name='Питання')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активне')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Опитування'
        verbose_name_plural = 'Опитування'

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('polls_app:detail', kwargs={'pk': self.pk})

    @property
    def total_votes(self):
        return sum(option.votes for option in self.options.all())


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200, verbose_name='Варіант відповіді')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    def percentage(self):
        total = self.poll.total_votes
        if not total:
            return 0
        return round(self.votes / total * 100, 1)
