from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.permissions import ModeratorRequiredMixin
from .models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    paginate_by = 15


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/detail.html'
    context_object_name = 'item'


class AnnouncementCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'priority']
    template_name = 'announcements/form.html'
    success_url = reverse_lazy('announcements:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Оголошення додано.')
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, ModeratorRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'priority']
    template_name = 'announcements/form.html'
    success_url = reverse_lazy('announcements:list')


class AnnouncementDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'announcements/confirm_delete.html'
    success_url = reverse_lazy('announcements:list')
