from users.models import User
from common.converters import ModelConverter


class UserConverter(ModelConverter):
    regex = r'[0-9]+'
    queryset = User.objects.select_related("profile").all()
    model_field = 'id'
