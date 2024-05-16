from rest_framework import permissions


# IsAdminOrReadOnly позволяет всем видеть запрос, а администраторам его удалять
class IsAdminOrReadOnly(permissions.BasePermission):
    # метод настраивает права доступа на уровне всего запроса
    def has_permission(self, request, view):
        # Прооверяем является ли запрос безопасным SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True
        # Берем проверку из класса IsAdminUser
        return bool(request.user and request.user.is_staff)


# IsOwnerOrReadOnly владельцы поста могут изменять, а остальные читать.
class IsOwnerOrReadOnly(permissions.BasePermission):
    # настраивает права доступа на уровне объекта.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # владелец поста == пользователю.
        return obj.user == request.user
