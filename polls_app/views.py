from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.forms import inlineformset_factory

from accounts.permissions import ModeratorRequiredMixin
from .models import Poll, PollOption

SESSION_VOTED_KEY = 'voted_polls'

PollOptionFormSet = inlineformset_factory(
    Poll, PollOption, fields=['text'], extra=3, can_delete=True, min_num=2, validate_min=True
)


class PollListView(ListView):
    model = Poll
    template_name = 'polls_app/list.html'
    context_object_name = 'polls'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Список опитувань, у яких користувач вже проголосував (зберігається в сесії)
        ctx['voted'] = self.request.session.get(SESSION_VOTED_KEY, [])
        return ctx


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls_app/detail.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        voted_polls = self.request.session.get(SESSION_VOTED_KEY, [])
        ctx['has_voted'] = self.object.pk in voted_polls
        return ctx


class PollVoteView(View):
    """Голосування із захистом від повторного голосу через Django sessions."""

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk, is_active=True)
        voted_polls = request.session.get(SESSION_VOTED_KEY, [])

        if poll.pk in voted_polls:
            messages.warning(request, 'Ви вже голосували в цьому опитуванні.')
            return redirect('polls_app:detail', pk=pk)

        option_id = request.POST.get('option')
        option = get_object_or_404(PollOption, pk=option_id, poll=poll)
        option.votes += 1
        option.save()

        voted_polls.append(poll.pk)
        request.session[SESSION_VOTED_KEY] = voted_polls
        request.session.modified = True

        messages.success(request, 'Дякуємо за вашу відповідь!')
        return redirect('polls_app:detail', pk=pk)


class PollCreateView(LoginRequiredMixin, ModeratorRequiredMixin, CreateView):
    model = Poll
    fields = ['question']
    template_name = 'polls_app/form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.POST:
            ctx['formset'] = PollOptionFormSet(self.request.POST)
        else:
            ctx['formset'] = PollOptionFormSet()
        return ctx

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        ctx = self.get_context_data()
        formset = ctx['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            messages.success(self.request, 'Опитування створено.')
            return redirect(self.object.get_absolute_url())
        return self.render_to_response(self.get_context_data(form=form))


class PollDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, DeleteView):
    model = Poll
    template_name = 'polls_app/confirm_delete.html'
    success_url = reverse_lazy('polls_app:list')
