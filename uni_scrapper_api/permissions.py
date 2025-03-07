from rest_framework import permissions


class IsStaffUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

