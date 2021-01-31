import django_filters
from my_app.models import Tournament

class TournamentFilter(django_filters.FilterSet):

    class Meta:
        model = Tournament
        fields = {
            'start_date': ['lt', 'gt']
        }