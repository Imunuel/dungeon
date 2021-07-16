import factory
import factory.fuzzy

from paths.models import Path
from textures.models import Texture


class PathFactory(factory.django.DjangoModelFactory):
    """Basic factory for path"""

    class Meta:
        model = Path


class TextureFactory(factory.django.DjangoModelFactory):
    """ Factory for texture that uses fake images template """

    class Meta:
        model = Texture

    image = factory.django.ImageField(
        color=factory.fuzzy.FuzzyChoice(['blue', 'yellow', 'green', 'orange']),
        height=factory.fuzzy.FuzzyInteger(10, 1000),
        width=factory.fuzzy.FuzzyInteger(10, 1000),
    )
