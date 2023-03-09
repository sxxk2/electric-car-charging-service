from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return view.kwargs.get("user_id") == request.user.id

    def has_object_permission(self, request, view, obj, **kwargs):
        return obj.user_id == request.user.id
