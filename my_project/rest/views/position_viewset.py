from rest_framework import viewsets

from my_app.models import Position
from rest.serializers import PositionSerializer


class PositionViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
