from rest_framework import serializers

from dungeons.models import Dungeon


class DungeonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dungeon
        fields = (
            'id',
            'title',
            'description',
            'position',
            'path'
        )
