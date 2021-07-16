import factory

from tests import factories
from dungeons.models import Dungeon


class DungeonFactory(factory.django.DjangoModelFactory):
    path = factory.SubFactory(factories.PathFactory)
    position = 10

    class Meta:
        model = Dungeon
