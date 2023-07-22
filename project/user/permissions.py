from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to see it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return obj.user == request.user or request.user.is_superuser
        else:
            # Check permissions for write request
            return obj.user == request.user or request.user.is_superuser

class IsOwnerOrReadOnlyForAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it and admins to do everything.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to the owner of the record, or if the user is an admin.
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user or request.user.is_staff

        # Write permissions are only allowed to the staff users (admin).
        return request.user.is_staff