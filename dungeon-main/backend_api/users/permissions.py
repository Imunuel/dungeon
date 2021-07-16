from rest_framework import permissions

from users.models import Profile


class IsObjectOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        obj = Profile.objects.get(user=view.kwargs['user'])
        return obj.user == request.user