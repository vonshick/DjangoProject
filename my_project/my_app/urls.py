from django.urls import path
from my_app.views import *

urlpatterns = [
    path('', NewLoginView.as_view(), name='index'),
    path('logout', NewLogoutView.as_view(), name='logout'),
    
    path('tournaments', AllTournamentView.as_view(), name="all_tournaments"),
    path('tournaments/add/', CreateTournamentView.as_view(), name="tournament_add"),
    path('tournaments/<int:pk>/update', UpdateTournamentView.as_view(), name="tournament_update"),
    path('tournaments/<int:pk>/', DetailTournamentView.as_view(), name="tournament_detail"),
    path('tournaments/<int:pk>/delete', DeleteTournamentView.as_view(), name="tournament_delete"),
    
    path('workers', WorkerListView.as_view(), name='all_workers'),
    path('workers/add/', CreateWorkerView.as_view(), name="worker_add"),
    path('workers/<int:pk>/update', UpdateWorkerView.as_view(), name="worker_update"),
    path('workers/<int:pk>/delete', DeleteWorkerView.as_view(), name="worker_delete"),
    path('avg_workers', AvgWorkersView.as_view(), name='avg_workers'),
]
