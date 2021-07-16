import factory

from tests import factories
from levels.models import Level


class LevelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Level