from django.urls import path
from my_app.views import *

urlpatterns = [
    path('', NewLoginView.as_view(), name='index'),
    path('register', CreateNewUserView.as_view(), name='register'),
    path('logout', NewLogoutView.as_view(), name='logout'),
    
    path('tournaments', AllTournamentView.as_view(), name="all_tournaments"),
    path('tournaments/add/', CreateTournamentView.as_view(), name="tournament_add"),
    path('tournaments/<int:pk>/update', UpdateTournamentView.as_view(), name="tournament_update"),
    path('tournaments/<int:pk>/', DetailTournamentView.as_view(), name="tournament_detail"),
    path('tournaments/<int:pk>/delete', DeleteTournamentView.as_view(), name="tournament_delete"),
    
    path('participants', ParticipantListView.as_view(), name='all_participants'),
    path('participants/add/', CreateParticipantView.as_view(), name="participant_add"),
    path('participants/<int:pk>/update', UpdateParticipantView.as_view(), name="participant_update"),
    path('participants/<int:pk>/delete', DeleteParticipantView.as_view(), name="participant_delete"),
]
