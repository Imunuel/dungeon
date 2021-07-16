from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from dungeons.models import Dungeon
from dungeons.serializers import DungeonDetailSerializer


class DungeonDetailApi(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Dungeon.objects.all()
    serializer_class = DungeonDetailSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
