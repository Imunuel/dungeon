from paths.models import Path
from common.converters import ModelConverter


class PathConverter(ModelConverter):
    regex = r'[0-9]+'
    queryset = Path.objects.all()
    model_field = 'id'

    def to_python(self, value: str) -> Path:
        try:
            return Path.objects.\
                prefetch_related("textures").\
                prefetch_related("dungeons").\
                get(id=value)
        except Path.DoesNotExist:
            raise ValueError('not exists')

    def to_url(self, value: Path) -> str:
        return str(value.id)
