from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from my_app.models import Position
from my_app import logger


class AllPositionView(LoginRequiredMixin, ListView):
    model = Position
    login_url = reverse_lazy('index')
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        logger.debug('AllPositionView.get_context_data')
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DetailPositionView(LoginRequiredMixin, DetailView):
    model = Position
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreatePositionView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Position
    fields = ['name', 'min_salary', 'max_salary']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_positions')
    login_url = reverse_lazy('index')


class UpdatePositionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Position
    fields = ['name', 'min_salary', 'max_salary']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_positions')
    login_url = reverse_lazy('index')


class DeletePositionView(LoginRequiredMixin, DeleteView):
    model = Position
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('all_positions')
