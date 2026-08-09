from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.permissions import ModeratorRequiredMixin
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/list.html'
    context_object_name = 'news_items'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'item'


class NewsCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'news/form.html'
    success_url = reverse_lazy('news:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Новину опубліковано.')
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, ModeratorRequiredMixin, UpdateView):
    model = News
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'news/form.html'
    success_url = reverse_lazy('news:list')


class NewsDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = News
    template_name = 'news/confirm_delete.html'
    success_url = reverse_lazy('news:list')
