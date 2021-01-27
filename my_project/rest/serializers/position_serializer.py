from rest_framework import serializers

from my_app.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name', 'min_salary', 'max_salary')
