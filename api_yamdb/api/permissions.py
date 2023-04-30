from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):
    """
    Может назначать роли пользователям.
    Может создавать и удалять произведения, категории, жанры.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_admin
                or request.user.is_superuser
            )
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Может создавать и удалять произведения, категории, жанры."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class IsAuthorOrModeratorOrAdminOrReadOnly(
    permissions.IsAuthenticatedOrReadOnly
):
    """Может удалять и редактировать любые отзывы и комментарии."""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )
