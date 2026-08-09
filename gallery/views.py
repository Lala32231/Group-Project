from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from accounts.permissions import ModeratorRequiredMixin
from .models import Album, Photo


class AlbumListView(ListView):
    model = Album
    template_name = 'gallery/list.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'gallery/detail.html'
    context_object_name = 'album'


class AlbumCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = Album
    fields = ['title']
    template_name = 'gallery/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PhotoCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'caption']
    template_name = 'gallery/photo_form.html'

    def form_valid(self, form):
        from django.shortcuts import get_object_or_404
        form.instance.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gallery:detail', kwargs={'pk': self.kwargs['pk']})


class AlbumDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = Album
    template_name = 'gallery/confirm_delete.html'
    success_url = reverse_lazy('gallery:list')
