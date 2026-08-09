from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import PortfolioItem


class PortfolioListView(ListView):
    model = PortfolioItem
    template_name = 'portfolio/list.html'
    context_object_name = 'items'
    paginate_by = 20


class PortfolioDetailView(DetailView):
    model = PortfolioItem
    template_name = 'portfolio/detail.html'
    context_object_name = 'item'


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioItem
    fields = ['title', 'description', 'file', 'link']
    template_name = 'portfolio/form.html'
    success_url = reverse_lazy('portfolio:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = PortfolioItem
    fields = ['title', 'description', 'file', 'link']
    template_name = 'portfolio/form.html'
    success_url = reverse_lazy('portfolio:list')

    def get_queryset(self):
        # Редагувати можна лише свої роботи (або адмін/модератор через адмінку)
        return PortfolioItem.objects.filter(owner=self.request.user)


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = PortfolioItem
    template_name = 'portfolio/confirm_delete.html'
    success_url = reverse_lazy('portfolio:list')

    def get_queryset(self):
        return PortfolioItem.objects.filter(owner=self.request.user)
