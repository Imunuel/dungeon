import factory

from invitations import models


class InvitationFactory(factory.django.DjangoModelFactory):
    """Basic factory for invite"""

    class Meta:
        model = models.Invitation
