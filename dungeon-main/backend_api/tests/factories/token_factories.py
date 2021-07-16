import factory
from django.contrib.auth import get_user_model
from rest_framework.authtoken import models as auth_models

from tests import factories

User = get_user_model()


class TokenFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(factories.UserFactory)


    class Meta:
        model = auth_models.Token