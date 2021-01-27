from rest_framework import serializers

from my_app.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'participants_limit', 'start_date', 'start_hour')
