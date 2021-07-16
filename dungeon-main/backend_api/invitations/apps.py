from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvitationsConfig(AppConfig):
    name = "invitations"
    verbose_name = _("Invitations")

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
