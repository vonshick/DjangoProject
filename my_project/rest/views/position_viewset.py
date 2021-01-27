from rest_framework import viewsets

from my_app.models import Tournament
from rest.serializers import TournamentSerializer


class TournamentViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
