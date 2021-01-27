from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, OuterRef, Subquery
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from my_app.models import Participant
from my_app.models import Tournament


class ParticipantListView(ListView):
    model = Participant

    @method_decorator(login_required(login_url=reverse_lazy('index')))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreateParticipantView(LoginRequiredMixin, CreateView):
    model = Participant
    fields = ('name', 'tournament')
    success_url = reverse_lazy('all_participants')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        name = form.data['name']
        tournament_id = form.data['tournament']
        tournament = Tournament.objects.filter(id=tournament_id).first()

        if name is None or name == '':
            messages.error(
                self.request,
                'The Name field can not be empty'
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            'New participant created successfully'
        )
        return super().form_valid(form)


class UpdateParticipantView(LoginRequiredMixin, UpdateView):
    model = Participant
    fields = ('name', 'tournament')
    success_url = reverse_lazy('all_participants')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        name = form.data['name']
        tournament_id = form.data['tournament']
        tournament = Tournament.objects.filter(id=tournament_id).first()

        if name is None or name == '':
            messages.error(
                self.request,
                'The Name field can not be empty'
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            'New participant updated successfully'
        )
        return super().form_valid(form)


class DeleteParticipantView(LoginRequiredMixin, DeleteView):
    model = Participant
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('all_participants')



