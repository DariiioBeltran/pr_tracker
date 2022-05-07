from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """This permission allows everyone to read it but 
    only the owner to update or delete it"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile == request.user