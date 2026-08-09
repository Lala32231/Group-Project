from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, UpdateView

from accounts.permissions import AdminRequiredMixin
from news.models import News
from forum.models import Topic
from events.models import Event
from announcements.models import Announcement
from polls_app.models import Poll
from gallery.models import Album

from .forms import SiteSettingsForm
from .models import SiteSettings


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['news_items'] = News.objects.filter(is_published=True)[:3]
        ctx['topics'] = Topic.objects.all()[:5]
        ctx['events'] = Event.objects.filter(date__gte=timezone.now())[:3]
        ctx['announcements'] = Announcement.objects.all()[:3]
        ctx['polls'] = Poll.objects.filter(is_active=True)[:2]
        ctx['albums'] = Album.objects.all()[:3]
        return ctx


class SiteSettingsView(AdminRequiredMixin, UpdateView):
    """Сторінка налаштувань порталу — зміна фону сайту (лише для адміністраторів)."""
    model = SiteSettings
    form_class = SiteSettingsForm
    template_name = 'core/settings.html'
    success_url = reverse_lazy('core:settings')

    def get_object(self):
        return SiteSettings.load()

    def form_valid(self, form):
        messages.success(self.request, 'Налаштування сайту оновлено.')
        return super().form_valid(form)
