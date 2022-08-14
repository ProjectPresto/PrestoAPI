from rest_framework import permissions


# If request is not authenticated, allow only GET, HEAD, OPTIONS requests.
# Else if request is authenticated, allow also POST, PUT and PATCH requests.
# Else if request is authenticated and user is staff, allow everything
class IsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ['POST', 'PUT', 'PATCH']:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_staff)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
