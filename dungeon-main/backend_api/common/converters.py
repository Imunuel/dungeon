from django.db.models import QuerySet, Model
from django.core.exceptions import ObjectDoesNotExist


class ModelConverter:
    regex: str = None
    queryset: QuerySet = None
    model_field: str = None

    def __init__(self):
        if None in (self.regex, self.queryset, self.model_field):
            raise AttributeError('ModelConverter attributes are not set')

    def to_python(self, value: str) -> Model:
        try:
            return self.queryset.get(**{self.model_field: value})
        except ObjectDoesNotExist:
            raise ValueError('not exists')

    def to_url(self, value) -> str:
        return str(getattr(value, self.model_field))
