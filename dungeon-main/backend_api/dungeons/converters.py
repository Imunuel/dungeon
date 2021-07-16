from dungeons.models import Dungeon
from common.converters import ModelConverter


class DungeonConverter(ModelConverter):
    regex = r'[0-9]+'
    queryset = Dungeon.objects.all()
    model_field = 'id'

    def to_python(self, value: str) -> Dungeon:
        try:
            return Dungeon.objects.get(id=value)
        except Dungeon.DoesNotExist:
            raise ValueError('not exists')

    def to_url(self, value: Dungeon) -> str:
        return str(value.id)
