from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, OuterRef, Subquery
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from my_app.models import Worker
from my_app.models import Tournament


class WorkerListView(ListView):
    model = Worker

    @method_decorator(login_required(login_url=reverse_lazy('index')))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreateWorkerView(LoginRequiredMixin, CreateView):
    model = Worker
    fields = ('name', 'salary', 'tournament')
    success_url = reverse_lazy('all_workers')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        salary = int(form.data['salary'])
        tournament_id = form.data['tournament']
        tournament = Tournament.objects.filter(id=tournament_id).first()

        if salary < tournament.min_salary or salary > tournament.max_salary:
            messages.error(
                self.request,
                'The salary must be between %d and %d' % (tournament.min_salary, tournament.max_salary)
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            'New worker created successfully'
        )
        return super().form_valid(form)


class UpdateWorkerView(LoginRequiredMixin, UpdateView):
    model = Worker
    fields = ('name', 'salary', 'tournament')
    success_url = reverse_lazy('all_workers')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        salary = int(form.data['salary'])
        tournament_id = form.data['tournament']
        tournament = Tournament.objects.filter(id=tournament_id).first()

        if salary < tournament.min_salary or salary > tournament.max_salary:
            messages.error(
                self.request,
                'The salary must be between %d and %d' % (tournament.min_salary, tournament.max_salary)
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            'New worker updated successfully'
        )
        return super().form_valid(form)


class DeleteWorkerView(LoginRequiredMixin, DeleteView):
    model = Worker
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('all_workers')


class AvgWorkersView(LoginRequiredMixin, TemplateView):
    template_name = 'my_app/avg_workers.html'
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Tournament.objects\
            .annotate(avg=Avg('worker__salary'))\
            .filter(id=OuterRef('tournament_id'))
        context['workers'] = Worker.objects\
            .filter(salary__gt=Subquery(query.values('avg'))).all()
        return context



