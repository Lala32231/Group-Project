from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.permissions import ModeratorRequiredMixin
from .models import Event


class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'
    context_object_name = 'events'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        now = timezone.now()
        ctx['upcoming'] = self.get_queryset().filter(date__gte=now)
        ctx['past'] = self.get_queryset().filter(date__lt=now)
        return ctx


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'


class EventCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']
    template_name = 'events/form.html'
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, ModeratorRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']
    template_name = 'events/form.html'
    success_url = reverse_lazy('events:list')


class EventDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/confirm_delete.html'
    success_url = reverse_lazy('events:list')
