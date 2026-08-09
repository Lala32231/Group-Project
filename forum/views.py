from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from accounts.permissions import ModeratorRequiredMixin
from .models import Topic, Post


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topics'
    paginate_by = 15


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title']
    template_name = 'forum/topic_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    http_method_names = ['post']

    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        if topic.is_closed:
            messages.error(self.request, 'Тема закрита для нових повідомлень.')
            return redirect(topic.get_absolute_url())
        form.instance.topic = topic
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('forum:topic_detail', kwargs={'pk': self.kwargs['pk']})


class TopicDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = Topic
    template_name = 'forum/confirm_delete.html'
    success_url = reverse_lazy('forum:topic_list')
