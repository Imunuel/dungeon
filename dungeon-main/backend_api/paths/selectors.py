from django.db.models.query import QuerySet

from paths.models import Path


def path_list() -> QuerySet[Path]:
    return Path.objects.all()
